class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0

        nums = [0] * (n + 1)
        nums[1] = 1

        for pos in range(2, len(nums)):
            if pos % 2 == 0:
                nums[pos] = nums[pos // 2]
            else:
                nums[pos] = nums[pos // 2] + nums[pos // 2 + 1]

        return max(nums)
