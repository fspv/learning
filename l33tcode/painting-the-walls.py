from functools import cache
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        max_cost = sum(cost) + 1

        @cache
        def dp(pos: int, occupied_time: int) -> int:
            if pos == len(cost):
                return 0 if occupied_time >= 0 else max_cost + 1

            return min(
                # Paint using the paid painter
                dp(pos + 1, min(occupied_time + time[pos], len(cost) - pos - 1))
                + cost[pos],
                # Paint for free
                dp(pos + 1, occupied_time - 1),
            )

        return dp(0, 0)
