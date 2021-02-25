from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack: List[int] = []
        first, last = len(nums), -1

        for pos in range(len(nums)):
            while stack and nums[stack[-1]] > nums[pos]:
                first = min(first, stack.pop())

            stack.append(pos)

        stack = []

        for pos in reversed(range(len(nums))):
            while stack and nums[stack[-1]] < nums[pos]:
                last = max(last, stack.pop())

            stack.append(pos)

        if first > last:
            return 0

        return last - first + 1
