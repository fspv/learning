import random
from typing import Tuple, List


class Rectangle:
    def __init__(
        self,
        bottom_left_row: int,
        bottom_left_col: int,
        top_right_row: int,
        top_right_col: int,
    ) -> None:
        self._bottom_left_row = bottom_left_row
        self._bottom_left_col = bottom_left_col
        self._top_right_row = top_right_row
        self._top_right_col = top_right_col

    @property
    def width(self) -> int:
        return self._top_right_col - self._bottom_left_col + 1

    @property
    def height(self) -> int:
        return self._top_right_row - self._bottom_left_row + 1

    @property
    def area(self) -> int:
        return self.width * self.height

    def get_coord_by_pos(self, pos: int) -> List[int]:
        return [
            self._bottom_left_col + (pos - 1) % self.width,
            self._bottom_left_row + (pos - 1) // self.width,
        ]


def find_rectangle_pos(number: int, partial_areas: List[int]) -> int:
    left, right = 0, len(partial_areas) - 1

    while left < right:
        middle = left + (right - left) // 2

        if partial_areas[middle] < number:
            left = middle + 1
        else:
            right = middle

    return left - 1


class Solution:
    def __init__(self, rects: List[List[int]]):
        self._partial_areas = [0]
        self._rects = []

        for rect in rects:
            rectangle = Rectangle(rect[1], rect[0], rect[3], rect[2])

            self._rects.append(rectangle)
            self._partial_areas.append(self._partial_areas[-1] + rectangle.area)

    def pick(self) -> List[int]:
        number = random.randint(1, self._partial_areas[-1])

        rectangle_pos = find_rectangle_pos(number, self._partial_areas)
        rectangle = self._rects[rectangle_pos]

        position = number - self._partial_areas[rectangle_pos]

        return rectangle.get_coord_by_pos(position)
