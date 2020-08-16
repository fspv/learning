from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return self.maxProfitDPTopDown(prices)
        # return self.maxProfitDPBottomUp(prices)

    def maxProfitDPBottomUp(self, prices: List[int]) -> int:
        operations = 2
        # 0 - bought, 1 - sold
        dp = [
            [[0] * (operations + 1) for _ in range(len(prices) + 1)],
            [[0] * (operations + 1) for _ in range(len(prices) + 1)],
        ]

        for price in reversed(range(len(prices))):
            for left in range(operations + 1):
                dp[0][price][left] = max(
                    dp[0][price + 1][left],
                    (dp[1][price + 1][left - 1] + prices[price]) if left > 0 else 0,
                )
                dp[1][price][left] = max(
                    dp[1][price + 1][left], dp[0][price + 1][left] - prices[price],
                )

        return dp[1][0][operations]

    def maxProfitDPTopDown(self, prices: List[int]) -> int:
        @lru_cache(None)
        def dfs(bought: bool, price: int, left: int) -> int:
            if price == len(prices) or left == 0:
                return 0

            result = 0

            if bought:
                result = max(
                    dfs(bought, price + 1, left),
                    dfs(not bought, price + 1, left - 1) + prices[price],
                )
            else:
                result = max(
                    dfs(bought, price + 1, left),
                    dfs(not bought, price + 1, left) - prices[price],
                )

            return result

        operations = 2
        return dfs(False, 0, operations)
