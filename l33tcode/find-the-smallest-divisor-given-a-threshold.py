import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def calc_sum(divisor: int) -> int:
            return sum(map(lambda num: math.ceil(num / divisor), nums))

        total = sum(nums)
        left, right = max(1, total // threshold), max(nums)

        while left < right:
            middle = left + (right - left) // 2

            if calc_sum(middle) > threshold:
                left = middle + 1
            else:
                right = middle

        return right
