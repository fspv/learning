class Solution:
    def maxProduct(self, nums):
        if not nums:
            return 0

        dp = set([nums[0]])
        result = nums[0]

        for pos in range(1, len(nums)):
            old_dp = dp
            dp = set([nums[pos]] + [res * nums[pos] for res in dp])
            result = max(result, max(dp))

        return result
