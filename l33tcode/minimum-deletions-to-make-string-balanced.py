from functools import lru_cache


class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = {True: 0, False: 0}

        for pos in range(len(s)):
            dp_old = dp
            dp = {True: float("+inf"), False: float("+inf")}

            if s[pos] == "b":
                dp[True] = min(dp[True], dp_old[True])
                dp[True] = min(dp[True], dp_old[False])
                dp[False] = min(dp[False], dp_old[False] + 1)
            else:
                dp[True] = min(dp[True], dp_old[True] + 1)
                dp[False] = min(dp[False], dp_old[False])

        return min(dp.values())

    def minimumDeletionsTopDown(self, s: str) -> int:
        @lru_cache(None)
        def dp(pos: int, b_taken: bool) -> int:
            if pos == len(s):
                return 0

            minimun_deletions = float("+inf")

            if s[pos] == "b":
                minimun_deletions = min(minimun_deletions, dp(pos + 1, True))
            elif not b_taken:
                minimun_deletions = min(minimun_deletions, dp(pos + 1, b_taken))

            minimun_deletions = min(minimun_deletions, dp(pos + 1, b_taken) + 1)

            return int(minimun_deletions)

        return dp(0, False)
