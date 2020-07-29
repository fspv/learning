from functools import lru_cache
from enum import Enum


class Solution:
    def maxProfitRecursive(self, prices: List[int]) -> int:
        class Phase(Enum):
            BUY = 0
            SELL = 1
            COOLDOWN = 2

        @lru_cache(None)
        def backtrack(pos: int, prev_phase: Phase) -> int:
            if pos == len(prices):
                return 0

            result = 0
            if prev_phase == Phase.COOLDOWN:
                result = max(result, backtrack(pos + 1, Phase.BUY) - prices[pos])
                result = max(result, backtrack(pos + 1, Phase.COOLDOWN))
            elif prev_phase == Phase.BUY:
                result = max(result, backtrack(pos + 1, Phase.SELL) + prices[pos])
                result = max(result, backtrack(pos + 1, Phase.BUY))
            elif prev_phase == Phase.SELL:
                result = max(result, backtrack(pos + 1, Phase.COOLDOWN))

            return result

        return backtrack(0, Phase.COOLDOWN)

    def maxProfit(self, prices: List[int]) -> int:
        buy = [0] * (len(prices) + 1)
        sell = [0] * (len(prices) + 1)
        cooldown = [0] * (len(prices) + 1)

        buy[0] = float("-inf")
        sell[0] = float("-inf")

        for pos in range(1, len(prices) + 1):
            cooldown[pos] = max(
                sell[pos - 1],
                cooldown[pos - 1],
            )
            buy[pos] = max(
                cooldown[pos - 1] - prices[pos - 1],
                buy[pos - 1],
            )
            sell[pos] = max(
                sell[pos - 1],
                buy[pos - 1] + prices[pos - 1],
            )

        return max(buy[-1], sell[-1], cooldown[-1])
