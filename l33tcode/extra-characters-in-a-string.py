from functools import cache
from typing import List


class Solution:
    def minExtraChar(self, string: str, words: List[str]) -> int:
        @cache
        def dp(pos: int) -> int:
            if pos == len(string):
                return 0

            # Skip symbol
            min_skip = dp(pos + 1) + 1

            for word in words:
                if string[pos : pos + len(word)] == word:
                    # Use word
                    min_skip = min(min_skip, dp(pos + len(word)))

            return min_skip

        return dp(0)
