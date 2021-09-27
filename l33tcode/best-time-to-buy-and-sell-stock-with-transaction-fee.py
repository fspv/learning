from functools import lru_cache
from typing import List


class Solution:
    def maxProfitBruteForce(self, prices: List[int], fee: int) -> int:
        def dp(pos: int, bought: bool) -> int:
            if pos == len(prices):
                return 0  # base case

            max_profit = 0

            if not bought:
                # Buy stock
                max_profit = max(max_profit, dp(pos + 1, True) - prices[pos] - fee)
            else:
                # Sell stock
                max_profit = max(max_profit, dp(pos + 1, False) + prices[pos])

            # Do nothing
            max_profit = max(max_profit, dp(pos + 1, bought))

            return max_profit

        return dp(0, False)

    def maxProfitTopDown(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dp(pos: int, bought: bool) -> int:
            if pos == len(prices):
                return 0  # base case

            max_profit = 0

            if not bought:
                # Buy stock
                max_profit = max(max_profit, dp(pos + 1, True) - prices[pos] - fee)
            else:
                # Sell stock
                max_profit = max(max_profit, dp(pos + 1, False) + prices[pos])

            # Do nothing
            max_profit = max(max_profit, dp(pos + 1, bought))

            return max_profit

        return dp(0, False)

    def maxProfitBottomUp(self, prices: List[int], fee: int) -> int:
        dp = [[0, 0] for _ in range(len(prices) + 1)]
        for pos in reversed(range(len(prices))):
            for bought in [True, False]:
                max_profit = 0

                if not bought:
                    # Buy stock
                    max_profit = max(max_profit, dp[pos + 1][True] - prices[pos] - fee)
                else:
                    # Sell stock
                    max_profit = max(max_profit, dp[pos + 1][False] + prices[pos])

                # Do nothing
                max_profit = max(max_profit, dp[pos + 1][bought])

                dp[pos][bought] = max_profit

        return dp[0][False]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = [0, 0]
        for pos in reversed(range(len(prices))):
            dp_old = dp
            dp = [0, 0]

            for bought in [True, False]:
                max_profit = 0

                if not bought:
                    # Buy stock
                    max_profit = max(max_profit, dp_old[True] - prices[pos] - fee)
                else:
                    # Sell stock
                    max_profit = max(max_profit, dp_old[False] + prices[pos])

                # Do nothing
                max_profit = max(max_profit, dp_old[bought])

                dp[bought] = max_profit

        return dp[False]
