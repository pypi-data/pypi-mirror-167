from typing import List

import pandas as pd
import geopandas as gpd
from shapely.geometry.base import BaseGeometry


def chunk_list(values_to_chunk: List, chunksize: int=10000):
    """
    :param values_to_chunk:
    :param chunksize:
    :return:
    """
    if chunksize is not None:
        for i in range(0, len(values_to_chunk), chunksize):
            yield values_to_chunk[i: i + chunksize]
    else:
        yield list


def merge_lists(list_of_lists: List) -> List:
    return list(zip(*list_of_lists))


def convert_geom_list_to_gdf(geom_list: List[BaseGeometry], epsg: int) -> gpd.GeoDataFrame:
    # output = df.DataFrame.from_records(geom_list, columns=['geometry'])
    output = pd.DataFrame()
    crs = {'init': 'epsg:%s' % epsg}
    output = gpd.GeoDataFrame(output, crs=crs, geometry=geom_list)

    return output
