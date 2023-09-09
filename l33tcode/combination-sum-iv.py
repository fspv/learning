from functools import cache
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
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
