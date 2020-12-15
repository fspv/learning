from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # find first non-negative element
        left, right = 0, len(nums)

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] < 0:
                left = middle + 1
            else:
                right = middle

        first_nonnegative = left

        # Construct result

        result: List[int] = []
        left, right = first_nonnegative - 1, first_nonnegative

        while left >= 0 or right < len(nums):
            if left >= 0 and right < len(nums):
                if -nums[left] < nums[right]:
                    result.append(nums[left] * nums[left])
                    left -= 1
                else:
                    result.append(nums[right] * nums[right])
                    right += 1
            elif left >= 0:
                result.append(nums[left] * nums[left])
                left -= 1
            else:
                result.append(nums[right] * nums[right])
                right += 1

        return result
