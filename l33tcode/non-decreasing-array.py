from typing import List
from functools import lru_cache


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def dfs(prev_pos: int, pos: int, skipped: bool) -> bool:
            if pos == len(nums):
                return True

            if skipped:
                if prev_pos == -1 or nums[prev_pos] <= nums[pos]:
                    return dfs(pos, pos + 1, True)
                else:
                    return False
            else:
                return (
                    (prev_pos == -1 or nums[prev_pos] <= nums[pos])
                    and dfs(pos, pos + 1, False)
                ) or dfs(prev_pos, pos + 1, True)

        return dfs(-1, 0, False)
