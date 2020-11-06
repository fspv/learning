from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        return min(
            sum(map(lambda pos: pos % 2, position)),
            sum(map(lambda pos: (pos + 1) % 2, position)),
        )
