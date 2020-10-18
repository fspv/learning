from functools import lru_cache


class Solution:
    def checkRecord(self, n: int) -> int:
        dp = [[1, 1, 1, 0], [1, 1, 1, 0], [0, 0, 0, 0]]
        mod = 10 ** 9 + 7

        for _ in range(n):
            old_dp = dp
            dp = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
            for absent in range(2):
                for late in range(3):
                    dp[absent][late] = (
                        (old_dp[absent + 1][0] + old_dp[absent][late + 1]) % mod
                        + old_dp[absent][0]
                    ) % mod

        return dp[0][0]

    def checkRecordTopDown(self, n: int) -> int:
        @lru_cache(None)
        def dp(pos: int, absent: int, late: int) -> int:
            if late > 2:
                return 0

            if absent > 1:
                return 0

            if pos == n:
                return 1

            return (
                dp(pos + 1, absent + 1, 0)
                + dp(pos + 1, absent, late + 1)
                + dp(pos + 1, absent, 0)
            )

        return dp(0, 0, 0) % (10 ** 9 + 7)
