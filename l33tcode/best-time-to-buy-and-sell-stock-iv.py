from typing import List
from functools import lru_cache


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def profit_unlimited_transactions() -> int:
            profit = 0

            min_cur, max_cur = prices[0] if prices else 0, prices[0] if prices else 0

            for price in range(1, len(prices)):
                if prices[price - 1] < prices[price]:
                    max_cur = prices[price]
                else:
                    profit += max_cur - min_cur

                    max_cur, min_cur = prices[price], prices[price]

            return profit + max_cur - min_cur

        def profit_limited_transactions() -> int:
            max_transactions = min((len(prices) + 1) // 2 + 1, k + 1)
            dp = [[0, 0] for _ in range(max_transactions)]
            max_profit = 0

            for price in reversed(range(len(prices))):
                max_transactions_cur = min((price + 1) // 2 + 1, k + 1)
                old_dp = dp
                dp = []
                for transactions in range(max_transactions_cur):
                    dp.append([0, 0])
                    for can_buy in [False, True]:
                        dp[transactions][can_buy] = max(
                            old_dp[transactions][can_buy],
                            old_dp[transactions + 1][False] - prices[price]
                            if can_buy and transactions < len(old_dp) - 1
                            else 0,
                            old_dp[transactions][True] + prices[price]
                            if not can_buy
                            else 0,
                        )

                max_profit = max(max_profit, dp[0][True])

            return max_profit

        if k > len(prices) // 2:
            return profit_unlimited_transactions()

        return profit_limited_transactions()

    def maxProfitTopDown(self, k: int, prices: List[int]) -> int:
        @lru_cache(None)
        def dp(price: int, transactions: int, can_buy: bool) -> int:
            if price == len(prices):
                return 0

            if transactions > k:
                return 0

            return max(
                dp(price + 1, transactions, can_buy),
                dp(price + 1, transactions + 1, False) - prices[price]
                if can_buy
                else 0,
                dp(price + 1, transactions, True) + prices[price] if not can_buy else 0,
            )

        return dp(0, 0, True)
