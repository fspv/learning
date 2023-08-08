from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid

        rotated_start = left % len(nums)

        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[(mid + rotated_start) % len(nums)] < target:
                left = mid + 1
            else:
                right = mid

        if nums[(pos := (left + rotated_start) % len(nums))] == target:
            return pos

        return -1
