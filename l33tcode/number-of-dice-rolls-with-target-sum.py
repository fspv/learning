from functools import lru_cache


class Solution:
    def numRollsToTarget(self, throws: int, faces: int, target: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def dp(left: int, num: int) -> int:
            if num < 0:
                return 0

            if left == 0:
                return int(num == 0)

            count = 0
            for face in range(1, faces + 1):
                count += dp(left - 1, num - face)

            return count % MOD

        return dp(throws, target)
