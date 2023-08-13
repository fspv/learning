from typing import List


class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [nums[-2] == nums[-1], False, True, False]

        for pos in reversed(range(len(nums) - 2)):
            dp = [False] + dp[:-1]
            dp[0] |= dp[2] & (nums[pos] == nums[pos + 1])
            dp[0] |= dp[3] & (nums[pos] == nums[pos + 1] == nums[pos + 2])
            dp[0] |= dp[3] & (nums[pos] == nums[pos + 1] - 1 == nums[pos + 2] - 2)

        return dp[0]
