from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        dp = [1] * len(nums)

        stack: List[int] = []

        for pos in range(len(nums)):
            while stack and nums[stack[-1]] < nums[pos]:
                dp[pos] = max(dp[pos], dp[stack.pop()] + 1)

            stack.append(pos)

        stack: List[int] = []

        for pos in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[pos]:
                stack.pop()

            if stack:
                dp[pos] = max(dp[pos], dp[stack[-1]] + 1)

            stack.append(pos)

        return any(map(lambda x: x > 2, dp))

    def increasingTripletN2(self, nums: List[int]) -> bool:
        dp = [1] * len(nums)

        stack: List[int] = []

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] < nums[right]:
                    dp[right] = max(dp[right], dp[left] + 1)

        return any(map(lambda x: x > 2, dp))
