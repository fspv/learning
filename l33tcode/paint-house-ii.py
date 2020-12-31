from typing import List
from functools import lru_cache


class Solution:
    def minCostII(self, costs: List[List[int]]) -> int:
        houses, colors = len(costs), len(costs[0]) if costs else 0

        dp = [0] * colors
        dp_min_pos = 0

        for house in range(houses):
            dp_old = dp
            dp_min_pos_old = dp_min_pos
            dp = [float("+inf")] * colors

            for color in range(colors):
                if color == dp_min_pos_old:
                    continue

                dp[color] = min(dp[color], dp_old[dp_min_pos_old] + costs[house][color])
                dp_min_pos = min(dp_min_pos, color, key=lambda pos: dp[pos])

            for next_color in range(colors):
                if dp_min_pos_old == next_color:
                    continue

                dp[dp_min_pos_old] = min(
                    dp[dp_min_pos_old],
                    dp_old[next_color] + costs[house][dp_min_pos_old],
                )

            dp_min_pos = min(dp_min_pos, dp_min_pos_old, key=lambda pos: dp[pos])

        if colors == 0:
            return 0

        if colors == 1:
            return costs[0][0]

        return dp[dp_min_pos]

    def minCostIITopDown(self, costs: List[List[int]]) -> int:
        houses, colors = len(costs), len(costs[0]) if costs else 0

        def dp(house: int, color: int) -> int:
            if house == houses - 1:
                return costs[house][color]

            min_cost = float("+inf")
            for next_color in range(colors):
                if next_color == color:
                    continue

                min_cost = min(
                    min_cost, dp(house + 1, next_color) + costs[house][color],
                )

            return min_cost

        if colors == 0:
            return 0

        return min([dp(0, color) for color in range(colors)])
