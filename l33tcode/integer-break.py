from functools import lru_cache


class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        for num in range(n + 1):
            for split in range(1, num // 2 + 1):
                dp[num] = max(
                    dp[num],
                    split * (num - split),
                    dp[split] * dp[num - split],
                    split * dp[num - split],
                    dp[split] * (num - split),
                )

        return dp[n]

    def integerBreakTopDown(self, n: int) -> int:
        @lru_cache(None)
        def dfs(num: int) -> int:
            result = 0

            for split in range(1, num // 2 + 1):
                result = max(
                    result,
                    split * (num - split),
                    dfs(split) * dfs(num - split),
                    split * dfs(num - split),
                    dfs(split) * (num - split),
                )

            return result

        return dfs(n)
