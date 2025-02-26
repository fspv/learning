class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        prev, prev_negative = 0, 0
        max_absolute_sum = 0

        for num in nums:
            prev += num
            prev_negative += num

            max_absolute_sum = max(max_absolute_sum, prev, -prev_negative)

            if prev < 0:
                prev = 0

            if prev_negative > 0:
                prev_negative = 0

        return max_absolute_sum
