from functools import lru_cache
from typing import Union


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def dp(pos1: int, pos2: int) -> Union[int, float]:
            if pos1 == len(s1) or pos2 == len(s2):
                if pos1 == len(s1) and pos2 == len(s2):
                    return 0
                elif pos1 == len(s1):
                    return dp(pos1, pos2 + 1) + ord(s2[pos2])
                else:
                    return dp(pos1 + 1, pos2) + ord(s1[pos1])

            min_ascii_sum = float("+inf")

            if s1[pos1] == s2[pos2]:
                min_ascii_sum = min(min_ascii_sum, dp(pos1 + 1, pos2 + 1))

            min_ascii_sum = min(min_ascii_sum, dp(pos1 + 1, pos2) + ord(s1[pos1]))
            min_ascii_sum = min(min_ascii_sum, dp(pos1, pos2 + 1) + ord(s2[pos2]))

            return min_ascii_sum

        return int(dp(0, 0))
