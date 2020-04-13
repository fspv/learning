from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        diff = 0
        diff_to_pos = {0: -1}
        result = 0

        for pos, num in enumerate(nums):
            diff += 1 if num else -1

            if diff not in diff_to_pos:
                diff_to_pos[diff] = pos
            else:
                result = max(result, pos - diff_to_pos[diff])

        return result
