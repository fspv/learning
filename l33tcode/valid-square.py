import operator
from typing import List, Tuple, DefaultDict
from collections import defaultdict


class Square:
    def __init__(self, points: List[Tuple[int, ...]]) -> None:
        self._points = points

    def validate(self) -> bool:
        points = self._points
        points.sort()

        vector1 = list(map(operator.sub, points[0], points[1]))
        vector1_len = sum(map(lambda x: x * x, vector1))
        vector2 = list(map(operator.sub, points[0], points[2]))
        vector2_len = sum(map(lambda x: x * x, vector2))
        vector3 = list(map(operator.sub, points[2], points[3]))
        vector3_len = sum(map(lambda x: x * x, vector3))
        vector4 = list(map(operator.sub, points[1], points[3]))
        vector4_len = sum(map(lambda x: x * x, vector4))

        return (
            vector1_len > 0
            and vector2_len > 0
            and vector3_len > 0
            and vector4_len > 0
            and vector1 == vector3
            and vector2 == vector4
            and vector1_len == vector2_len
            and (
                (vector1[0] == vector2[1] and vector1[1] == -vector2[0])
                or (vector1[0] == -vector2[1] and vector1[1] == vector2[0])
            )
        )


class Solution:
    def validSquare(
        self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]
    ) -> bool:
        square = Square([tuple(p1), tuple(p2), tuple(p3), tuple(p4)])

        return square.validate()
