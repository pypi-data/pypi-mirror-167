from geospatial_lib.core.core import GeoLibCore
from geospatial_lib.db.pg_handler import PgHandler
from geospatial_lib.db.pandas_handler import PandasHandler


class GeoSpatialLib(GeoLibCore, PgHandler, PandasHandler):

    def __init__(self, *args, **kwargs):
        """
        Main Constructor

        :param logger_name: personalize the logger name
        :type logger_name: str
        :param logger_dir: path to store the log
        :type logger_dir: str
        """
        super().__init__(*args, **kwargs)
