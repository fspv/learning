class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        return nums[left % len(nums)]
