from typing import List
from functools import lru_cache


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()

        @lru_cache(None)
        def dp(pos: int) -> bool:
            if pos in visited:
                return False

            if pos < 0 or pos >= len(arr):
                return False

            if arr[pos] == 0:
                return True

            visited.add(pos)

            return dp(pos + arr[pos]) or dp(pos - arr[pos])

        return dp(start)
