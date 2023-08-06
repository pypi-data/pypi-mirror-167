from typing import List
from typing import Dict

import io

import sys

import psycopg2

from sqlalchemy import exc
from sqlalchemy_utils import database_exists
from sqlalchemy_utils import create_database
from sqlalchemy_utils import drop_database
from sqlalchemy.schema import CreateSchema

from geospatial_lib.db.pg_core import PgCore
from geospatial_lib.misc.helpers import chunk_list


class PgHandler(PgCore):
    """
    Class : PgHandler
    """

    _DEFAULT_CHUNKSIZE = 10000
    logger = None

    def init_db(self, host: str, database: str, username: str, password: str, port: str, extensions: List[str], overwrite: bool) -> Dict:
        """
        Initialize a DB:
            - create
            - overwrite
            - get session and engine

        :type host: str
        :type port: int
        :type database: str
        :type username: str
        :type password: str
        :type extensions: str
        :type overwrite: bool, default: false

        :return: dict with this following keys session, engine  ; session db and engine db
        :rtype: dict {class 'sqlalchemy.orm.session.Session', <class 'sqlalchemy.engine.base.Engine'>}
        """

        try:
            session, engine = self.sqlalchemy_connection(
                host=host, database=database, username=username, password=password, port=port
            )

        except Exception as ex:
            self.logger.warning(f"{type(ex).__name__}: Engine NOK (Arguments: {ex.args})")
            raise ex

        try:
            if database_exists(engine.url):
                self.logger.warning(f"Database {database} exists")
                if overwrite:
                    self.logger.warning(
                        f"Overwrite is True => Database {database} dropped"
                    )
                    drop_database(engine.url)
                    self.init_db(
                        host,
                        database,
                        username,
                        password,
                        port,
                        extensions,
                        overwrite,
                    )

            else:
                self.logger.info(f"Database : {database} created!")
                create_database(engine.url)

                for name in extensions:
                    try:
                        engine.execute(f"create extension {name}")
                    except Exception as err:
                        raise ValueError(
                            f"{type(err).__name__}: extensions declaration error (args: {err.args})"
                        )
        except exc.OperationalError as ex:
            self.logger.warning(f"Oops default db postgres does not exists : {ex}")

        return {"session": session, "engine": engine}

    def psycopg2_connection(self, host: str, database: str, username: str, password: str, port: str):
        """
        Get the DB psycopg2 connection

        :type database: string
        :type username: string
        :type host: string
        :type password: string
        :type port: str
        :return:
        """
        connection = psycopg2.connect(
            dbname=database, user=username, host=host, password=password, port=port
        )

        return connection

    def init_schema(self, engine, schema: str) -> bool:
        """
        Create a schema

        :param engine: db engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'
        :param schema: the schema name to create
        :type schema: str

        :return: Check if schema exists
        :rtype: bool
        """
        is_exists = False
        try:
            engine.execute(CreateSchema(schema))
            self.logger.info(f"Creating {schema} schema")

        except exc.ProgrammingError as err:
            self.logger.info(f"Schema {schema} cannot be created {err}")
            is_exists = True

        return is_exists


    def sql_query_to_list(self, query):
        """
        To convert a sqlAlchemy query to a list of dicts with columns and thier value

        :param query: a sqlAlchemy query
        :type query: class 'sqlalchemy.orm.query.Query'

        :return: the converted query
        :rtype: list of dicts
        """

        return [
            {
                column: getattr(row, column)
                for column in row._fields
            }
            for row in query.all()
        ]

    def dict_list_to_db(self, engine, data: List[Dict], schema: str, table_name: str, chunk_size: int=_DEFAULT_CHUNKSIZE):
        """
        Write a list of dicts into a DB (postgres)

        :param engine: db engine
        :type engine: <class 'sqlalchemy.engine.base.Engine'
        :param data: the data to write into the db
        :type data: list of dicts
        :param schema: schema name
        :type schema: str
        :param table_name: table name
        :type table_name: str
        :param chunk_size: chunk size, default 10000
        :type chunk_size: int

        """
        def write_into_db_process(input_data: List[Dict]) -> None:
            columns = ', '.join('"{}"'.format(k) for k in list(data[0].keys()))
            with conn.cursor() as cursor:
                f = IteratorFile(("\t".join(row.values()) for row in input_data))
                sql_copy = f"COPY {schema}.{table_name} ({columns}) FROM STDIN WITH CSV DELIMITER E'\t' QUOTE E'\b' NULL AS ''"
                cursor.copy_expert(sql_copy, f)
                conn.commit()

        data_chunked = chunk_list(data, chunk_size)

        credential_from_engine = engine.url
        conn = self.psycopg2_connection(
            database=credential_from_engine.database,
            username=credential_from_engine.username,
            host=credential_from_engine.host,
            password=credential_from_engine.password,
            port=credential_from_engine.port,
        )

        total_features = len(data)
        features_writed = 0
        for data in data_chunked:

            write_into_db_process(data)
            features_writed += len(data)
            self.logger.info(f"{features_writed}/{total_features} writed!")


class IteratorFile(io.TextIOBase):
    """
    In order to create an "sql file" to improve db writing

    """
    ## from https://gist.github.com/jsheedy/ed81cdf18190183b3b7d
    def __init__(self, it):
        self._it = it
        self._temp_file = io.StringIO()

    def read(self, length=sys.maxsize):

        try:
            while self._temp_file.tell() < length:
                self._temp_file.write(next(self._it) + "\n")

        except StopIteration as _:
            pass

        except Exception as e:
            print("uncaught exception: {}".format(e))

        finally:
            self._temp_file.seek(0)
            data = self._temp_file.read(length)

            # save the remainder for next read
            remainder = self._temp_file.read()
            self._temp_file.seek(0)
            self._temp_file.truncate(0)
            self._temp_file.write(remainder)
            return data

    def readline(self):
        return next(self._it)
