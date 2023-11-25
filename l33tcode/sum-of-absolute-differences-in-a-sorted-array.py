from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        nums.sort()  # so the absolute diff is calculated correctly

        result: List[int] = [0] * len(nums)

        # left->right
        diff = 0
        for pos in range(len(nums)):
            diff += (nums[pos] - nums[pos - 1]) * pos
            result[pos] += diff

        # right->left
        diff = 0
        for pos in range(len(nums)):
            diff += (nums[-pos] - nums[-pos - 1]) * pos
            result[-pos - 1] += diff

        return result
