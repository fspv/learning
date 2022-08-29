from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class Point:
    x: int
    y: int
    covered: bool = False

    def covers(self, other: Point) -> bool:
        return self.y - abs(self.x - other.x) >= other.y


class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        """
        Don't really need a stack here, just the last point which has
        the longest slope will work. Actually this problem can be reduced
        to the merge intervals problem
        """
        points: List[Point] = [Point(x, y) for x, y in sorted(peaks)]

        stack: List[Point] = []

        for point in points:
            while stack and point.covers(stack[-1]):
                stack[-1].covered = True

                if stack[-1] == point:
                    point.covered = True

                stack.pop()

            if stack and stack[-1].covers(point):
                point.covered = True
            else:
                stack.append(point)

        return sum(not point.covered for point in points)
