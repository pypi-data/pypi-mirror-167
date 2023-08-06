from shapely import geos

from json import dumps

import xlrd

import pandas as pd
import geopandas as gpd

from shapely.geometry.base import BaseGeometry

from geoalchemy2 import Geometry
from sqlalchemy import select

from psycopg2.extras import DateTimeRange
from datetime import datetime

from geospatial_lib.db.pg_core import PgCore


class PandasHandler(PgCore):

    _GEOMETRY_FIELD = "geometry"
    _IF_TABLE_EXISTS = "append"
    _INDEX = False
    _IS_FIRST_WRITE = False

    logger = None

    def df_from_table(self, engine, schema: str, table: str):
        """
        Create a dataframe from a sql table

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str

        :return: the db table to a dataframe:
        :rtype: pandas.Dataframe
        """

        metadata = self._get_metadata(engine, schema)
        try:
            self.logger.info(f"Load Dataframe from db: '{schema}'.{table}")
            table_conn = metadata.tables[f"{schema}.{table}"]
            return pd.read_sql_query(select([table_conn]), con=engine)

        except Exception as ex:
            raise ex

    def gdf_from_table(self, engine, schema: str, table: str, geom_col: str=_GEOMETRY_FIELD):
        """
        Create a geodataframe from a sql table

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str
        :param geom_col: the geometry column name
        :type geom_col: str

        :return: the db table to a dataframe:
        :rtype: pandas.Dataframe
        """
        metadata = self._get_metadata(engine, schema)
        try:
            self.logger.info(f"Load Geodataframe from db: '{schema}'.{table}")
            table_conn = metadata.tables[f"{schema}.{table}"]
            return gpd.GeoDataFrame.from_postgis(
                "SELECT * FROM " + str(table_conn), con=engine, geom_col=geom_col
            )

        except Exception as ex:
            raise ex

    def df_from_xlrd(self, xls_path: str, sheet_name: str, header_row: int=0, encoding: str="utf-8", on_demand: bool=True):
        """
        Create a dataframe from a file

        :type xls_path: str
        :type sheet_name: str
        :type header_row: int, optional

        :return:
        :rtype: geopandas.Dataframe
        """
        workbook = xlrd.open_workbook(
            xls_path, encoding_override=encoding, on_demand=on_demand
        )
        sheet_data = workbook.sheet_by_name(sheet_name)

        first_row = [
            sheet_data.cell_value(header_row, column)
            for column in range(sheet_data.ncols)
        ]
        data = [
            {
                first_row[col]: sheet_data.cell_value(row, col)
                for col in range(sheet_data.ncols)
            }
            for row in range(header_row + 1, sheet_data.nrows)
        ]

        return pd.DataFrame(data)

    def gdf_from_files(self, files, polygon=None, fields_to_keep=None):
        """
        Create a geodataframe from a file

        :type files: list of str
        :type polygon: shapely.geometry.Polygon
        :type fields_to_keep: list

        :return:
        :rtype: geopandas.Geodataframe
        """
        polygon_bounds = None
        if polygon is not None:
            polygon_bounds = polygon.bounds

        if fields_to_keep is None:
            fields_to_keep = slice(None)

        output_gdf = pd.concat(
            [
                gpd.read_file(file_path, bbox=polygon_bounds)[fields_to_keep]
                for file_path in files
            ]
        )

        if polygon is not None:
            # TODO optimize
            output_gdf = output_gdf.loc[
                output_gdf["geometry"].intersects(polygon)
            ]

        return output_gdf

    def __is_output_table_empty(self, engine, schema: str, table: str, is_first_write: bool):
        is_filled, rows_count = self._is_sql_table_filled(engine, schema, table)
        self.logger.info(f"Count {rows_count} features on '{schema}'.{table}")

        if is_first_write and is_filled:
            raise Exception(
                f"Writing DF to SQL - is_first_write is {is_first_write}: features already exists..."
            )

    def __clean_df_fields_with_output_table(self, gdf, sql_table):
        # check column format and clean gdf
        output_table_columns = {
            column.name.casefold(): column.name for column in sql_table.c
        }

        columns_to_rename = {}
        for gdf_column in gdf.columns:
            gdf_column_casefold = gdf_column.casefold()
            if gdf_column_casefold in output_table_columns:
                columns_to_rename[gdf_column] = output_table_columns[
                    gdf_column_casefold
                ]

        gdf = gdf.rename(columns=columns_to_rename)
        # remove useless columns
        gdf = gdf[columns_to_rename.values()]

        return gdf

    def gdf_design_checker(
        self,
        engine,
        schema: str,
        table: str,
        data,
        epsg: int,
        geometry_field: str=_GEOMETRY_FIELD,
        if_table_exists: bool=_IF_TABLE_EXISTS,
        index: int=_INDEX,
        is_first_write: bool=_IS_FIRST_WRITE,
    ):
        """
        in order to create a sql table regarding geodataframe format

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str
        :param data: geodataframe to check
        :type data: geopandas.GeoDataFrame
        :param epsg: EPSG value
        :type epsg: int
        :param geometry_field: the geom column name, default geometry
        :type geometry_field: str, default geometry
        :param if_table_exists: "replace" or "append" ; "replace" can mean "create"
        :type: str
        :type index: bool, default False
        :type is_first_write: bool

        :return: geodataframe cleaned
        :rtype data: geopandas.GeoDataFrame
        """

        self.logger.info(f"Preparing writing GDF into '{schema}'.{table}...")

        type_geom = data[geometry_field].iloc[0].geom_type

        if if_table_exists == "append":
            # verify if data is compatible and update it
            self.__is_output_table_empty(engine, schema, table, is_first_write)
            output_table = self.table_from_name(engine, schema, table)
            data = self.__clean_df_fields_with_output_table(data, output_table)
            self.logger.info(f"GeoDataframe compatible with table '{schema}'.{table}")

        else:
            data[:0].to_sql(
                name=table,
                con=engine,
                schema=schema,
                if_exists=if_table_exists,
                index=index,
                dtype={geometry_field: Geometry(type_geom, srid=epsg)},
            )
            self.logger.info(f"The table '{schema}'.{table} is created.")

        return data

    def df_design_checker(
        self,
        engine,
        schema: str,
        table: str,
        data,
        if_table_exists: bool=_IF_TABLE_EXISTS,
        index: int=_INDEX,
        is_first_write: bool=_IS_FIRST_WRITE,
    ):
        """
        in order to create a sql table regarding dataframe format

        :param engine: DB engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'>
        :param schema: schema name
        :type schema: str
        :param table: table name
        :type table: str
        :param data: dataframe to check
        :type data: pandas.DataFrame
        :param if_table_exists: "replace" or "append" ; "replace" can mean "create"
        :type: str
        :type index: bool, default False
        :type is_first_write: bool

        :return: geodataframe cleaned
        :rtype data: geopandas.GeoDataFrame
        """
        self.logger.info(f"Preparing writing DF into '{schema}'.{table}...")

        if if_table_exists == "append":
            # verify if data is compatible and update it
            self.__is_output_table_empty(engine, schema, table, is_first_write)
            output_table = self.table_from_name(engine, schema, table)
            data = self.__clean_df_fields_with_output_table(data, output_table)
            self.logger.info(f"Dataframe compatible with table '{schema}'.{table}")

        else:
            data[:0].to_sql(
                name=table,
                con=engine,
                schema=schema,
                index=index,
                if_exists=if_table_exists,
            )
            self.logger.info(f"The table '{schema}'.{table} is created.")

        return data

    def df_to_dicts_list(self, data, epsg=None):
        """
        Convert a dataframe or a geodataframe to a list of dicts

        :param data: input data
        :type data: pandas.Dataframe / geopandas.GeoDataframe
        :param epsg: EPSG value, only if a geodataframe is used
        :type epsg: int

        :return: the dataframe converted into a list of dicts
        :rtype: list of dicts
        """
        _datetime_infinite_value = ""

        self.logger.info(
            f"Prepare {data.shape[0]} features ; columns: {data.columns.tolist()}"
        )

        lambda_functions_by_types = {
            # TODO simplify
            "DateTimeRange": lambda x: f"{x._bounds[0]}{str(x.lower) if x.lower is not None else _datetime_infinite_value},"
            f"{str(x.upper) if x.upper is not None else _datetime_infinite_value}{x._bounds[-1]}",
            "datetime": lambda x: x.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "BaseGeometry": lambda x: self.__convert_shapely_to_ewkb(x, epsg),
            "dict": lambda x: dumps(x, ensure_ascii=False),
            "list": lambda x: "{}" if len(x) == 0 else '{' + ', '.join(f'"{feat}"' for feat in x) + '}',
            "default": lambda x: x.__str__(),
        }

        for column in data.columns:
            first_element = data[column].iat[0]
            if isinstance(first_element, DateTimeRange):
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["DateTimeRange"]
                )

            elif isinstance(first_element, datetime):
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["datetime"]
                )

            elif isinstance(first_element, BaseGeometry):
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["BaseGeometry"]
                )

            elif isinstance(first_element, dict):
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["dict"]
                )

            elif isinstance(first_element, list):
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["list"]
                )

            else:
                data.loc[:, column] = data[column].map(
                    lambda_functions_by_types["default"]
                )

        return data.to_dict("records")

    def df_explode_datetimerange_fields(self, data):
        """
        Explode DateTimeRange type column into 2 datetime columns (start_date & end_date)

        :param data: input data
        :type data: pandas.Dataframe / geopandas.GeoDataframe

        :return: input data
        :rtype: pandas.Dataframe / geopandas.GeoDataframe

        """
        _min_datetime = pd.Timestamp.min
        _max_datetime = pd.Timestamp.max

        columns_to_remove = []
        for column in data.columns:

            value = data[column].values[0]

            if isinstance(value, DateTimeRange):
                data.loc[:, f"{column}__start_date"] = data[column].apply(
                    lambda x: _min_datetime if x.lower is None else x.lower
                )

                data.loc[:, f"{column}__end_date"] = data[column].apply(
                    lambda x: _max_datetime if x.upper is None else x.upper
                )

                columns_to_remove.append(column)

        if len(columns_to_remove) > 0:
            data = data.drop(columns=columns_to_remove)

        return data

    @staticmethod
    def __convert_shapely_to_ewkb(geometry, epsg: int):
        if not isinstance(epsg, int):
            raise ValueError(f"Check epsg type value: {type(epsg)} found")

        # set env values
        geos.WKBWriter.defaults["include_srid"] = True
        geos.lgeos.GEOSSetSRID(geometry._geom, epsg)
        return geometry.wkb_hex
