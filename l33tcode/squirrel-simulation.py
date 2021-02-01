import math
from typing import List


class Solution:
    def minDistance(
        self,
        height: int,
        width: int,
        tree: List[int],
        squirrel: List[int],
        nuts: List[List[int]],
    ) -> int:
        def distance(x1: int, y1: int, x2: int, y2: int) -> int:
            return abs(x1 - x2) + abs(y1 - y2)

        total = 0.0
        min_diff = float("+inf")

        for x, y in nuts:
            nut_to_tree = distance(x, y, tree[0], tree[1])
            nut_to_squirrel = distance(x, y, squirrel[0], squirrel[1])

            total += nut_to_tree * 2
            min_diff = min(min_diff, nut_to_squirrel - nut_to_tree)

        return int(total + min_diff)
