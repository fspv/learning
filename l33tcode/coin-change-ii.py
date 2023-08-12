from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for pos in range(1, amount + 1):
                if pos - coin >= 0:
                    dp[pos] += dp[pos - coin]

        return dp[amount]
