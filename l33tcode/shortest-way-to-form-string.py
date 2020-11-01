from functools import lru_cache


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        @lru_cache(None)
        def dp(source_pos: int, target_pos: int) -> int:
            if target_pos == len(target):
                return int(source_pos != 0)

            min_subsequences = float("+inf")

            if source[source_pos] != target[target_pos]:
                min_subsequences = min(
                    min_subsequences,
                    dp((source_pos + 1) % len(source), target_pos)
                    + (source_pos + 1) // len(source),
                )
            else:
                min_subsequences = min(
                    min_subsequences,
                    dp((source_pos + 1) % len(source), target_pos + 1)
                    + (source_pos + 1) // len(source),
                )

            return min_subsequences

        if set(target) - set(source):
            return -1

        return dp(0, 0)
