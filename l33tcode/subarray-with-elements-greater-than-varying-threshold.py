from typing import List


class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        stack: List[int] = []

        prev_smaller: List[int] = [-1] * len(nums)
        next_smaller: List[int] = [len(nums)] * len(nums)

        for pos in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[pos]:
                stack.pop()

            if stack:
                prev_smaller[pos] = stack[-1]

            stack.append(pos)

        stack.clear()

        for pos in reversed(range(len(nums))):
            while stack and nums[stack[-1]] >= nums[pos]:
                stack.pop()

            if stack:
                next_smaller[pos] = stack[-1]

            stack.append(pos)

        result = -1

        for pos in range(len(nums)):
            if nums[pos] > threshold / (next_smaller[pos] - prev_smaller[pos] - 1):
                result = next_smaller[pos] - prev_smaller[pos] - 1

        return result

    def validSubarraySizeBruteForce(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)

        if min(nums) > threshold // len(nums):
            return len(nums)

        for left in range(len(nums)):
            min_val = max_num

            for right in range(left, len(nums)):
                min_val = min(nums[right], min_val)

                if min_val > threshold / (right - left + 1):
                    return right - left + 1

        return -1
