from typing import List
from functools import lru_cache


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @lru_cache(None)
        def dp(pos: int) -> int:
            if pos >= len(cost):
                return 0

            return min(dp(pos + 1) + cost[pos], dp(pos + 2) + cost[pos],)

        return min(dp(0), dp(1))
