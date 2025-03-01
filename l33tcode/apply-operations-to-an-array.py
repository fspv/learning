class Solution:
    def applyOperations(self, nums: list[int]) -> list[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

        ptr = 0

        for pos, num in enumerate(nums):
            if num != 0:
                nums[ptr], nums[pos] = nums[pos], nums[ptr]
                ptr += 1

        return nums
