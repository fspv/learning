from functools import lru_cache


class Solution:
    def numDistinct(self, source: str, target: str) -> int:
        @lru_cache(None)
        def dp(source_pos: int, target_pos: int) -> int:
            if target_pos == len(target):
                return 1

            if source_pos == len(source):
                return 0

            ways = 0

            if source[source_pos] == target[target_pos]:
                ways += dp(source_pos + 1, target_pos + 1)

            ways += dp(source_pos + 1, target_pos)

            return ways

        return dp(0, 0)
