from geospatial_lib.core.logger import Logger


class GeoLibCore(Logger):

    def __init__(self, *args, **kwargs):
        """
        Main Constructor

        :param logger_name: personalize the logger name
        :type logger_name: str
        :param logger_dir: path to store the log
        :type logger_dir: str
        """
        super().__init__(*args, **kwargs)
