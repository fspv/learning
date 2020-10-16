from typing import List
from functools import lru_cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def dfs(total: int) -> int:
            if total > target:
                return 0

            if total == target:
                return 1

            count = 0
            for num in nums:
                count += dfs(total + num)

            return count

        return dfs(0)
