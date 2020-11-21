from typing import List


class Solution:
    def solve(self, nums: List[int], pos: int) -> int:
        stack: List[int] = []

        nums.append(0)
        max_area = max(nums[pos], min(nums) * len(nums))

        for right_pos in range(len(nums)):
            while stack and nums[stack[-1]] > nums[right_pos]:
                height = nums[stack.pop()]
                left_pos = stack[-1] + 1 if stack else 0
                area = (right_pos - left_pos) * height

                if left_pos <= pos < right_pos:
                    max_area = max(max_area, area)

            stack.append(right_pos)

        return max_area
