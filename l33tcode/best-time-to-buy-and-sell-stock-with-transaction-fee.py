from functools import lru_cache


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = float("-inf"), 0

        for pos, price in enumerate(prices):
            buy_prev, sell_prev = buy, sell
            buy = max(buy_prev, sell_prev - price)
            sell = max(sell_prev, buy_prev + price - fee)

        return sell

    def maxProfitTopDown(self, prices: List[int], fee: int) -> int:
        @lru_cache(None)
        def dfs(pos, total, bought):
            if pos == len(prices):
                return total

            result = dfs(pos + 1, total, bought)

            if bought:
                result = max(result, dfs(pos + 1, total + prices[pos] - fee, False))
            else:
                result = max(result, dfs(pos + 1, total - prices[pos], True))

            return result

        return dfs(0, 0, False)
