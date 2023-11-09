from functools import cache

MOD = 10 ** 9 + 7


class Solution:
    def countHomogenous(self, s: str) -> int:
        @cache
        def dp(pos: int) -> int:
            count = 1

            if pos + 1 < len(s) and s[pos] == s[pos + 1]:
                count += dp(pos + 1)

            return count % MOD

        return sum([dp(pos) for pos in range(len(s))]) % MOD
