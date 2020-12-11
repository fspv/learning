from typing import DefaultDict, List, Tuple, Counter
from collections import defaultdict


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(left: int, right: int) -> int:
            while right != 0:
                left, right = right, left % right

            return left

        max_points = 0

        for point1 in range(len(points)):
            x1, y1 = points[point1]
            params: DefaultDict[Tuple[int, int], int] = defaultdict(lambda: 0)
            point1_count = 0

            for point2 in range(point1, len(points)):
                x2, y2 = points[point2]

                if (x1, y1) == (x2, y2):
                    point1_count += 1
                else:
                    delta_gcd = gcd(y2 - y1, x2 - x1)
                    params[((y2 - y1) // delta_gcd, (x2 - x1) // delta_gcd)] += 1

            max_points = max(
                max_points, max(list(params.values()) or [0]) + point1_count
            )

        return max_points
