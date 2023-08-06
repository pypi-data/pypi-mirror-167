import math
from typing import Any, List, Tuple

from shapely.geometry import Polygon
from shapely import affinity


class Gridding:
    __slots__ = (
        "_xmin",
        "_xmax",
        "_ymin",
        "_ymax",
        "_length_x",
        "_length_y",
        "_output_geometries"
    )

    def __init__(self, input_polygon: Any, length_x: int, length_y: int) -> None:

        self._xmin: float = input_polygon.bounds[0]
        self._xmax: float = input_polygon.bounds[2]
        self._ymin: float = input_polygon.bounds[1]
        self._ymax: float = input_polygon.bounds[3]
        self._length_x: int = length_x
        self._length_y: int = length_y

        # output list
        self._output_geometries = []
        
    def run(self) -> List[Polygon]:
        rows, columns = self._compute_rows_and_columns_number()
        x_left_origin, x_right_origin, y_top_origin, y_bottom_origin = self._get_origin_grid()

        # create grids
        print(columns, rows)
        for _ in range(0, columns):

            # reset Y coords, go to east beginning to the top
            y_top = y_top_origin
            y_bottom = y_bottom_origin

            for _ in range(0, rows):

                points_list = [
                    (x_left_origin, y_top),
                    (x_right_origin, y_top),
                    (x_right_origin, y_bottom),
                    (x_left_origin, y_bottom)
                ]

                self._output_geometries.append(Polygon(points_list))

                # next poly to the south
                y_top -= self._length_y
                y_bottom -= self._length_y

            # news X coords to next poly to the east
            x_left_origin += self._length_x
            x_right_origin += self._length_x

            return self._output_geometries

    def _compute_rows_and_columns_number(self) -> Tuple[int, int]:

        # get nb of rows
        rows = math.ceil((self._ymax - self._ymin) / self._length_y)
        # get nb ob columns
        columns = math.ceil((self._xmax - self._xmin) / self._length_x)
        
        return rows, columns
    
    def _get_origin_grid(self) -> Tuple[float, float, float, float]:

        # start grid envelope
        x_left_origin = self._xmin
        x_right_origin = self._xmin + self._length_x
        y_top_origin = self._ymax
        y_bottom_origin = self._ymax - self._length_y

        return x_left_origin, x_right_origin, y_top_origin, y_bottom_origin
