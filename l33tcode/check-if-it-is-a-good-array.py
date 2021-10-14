from typing import List


class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        def gcd(x: int, y: int) -> int:
            if y == 0:
                return x

            return gcd(y, x % y)

        if not nums:
            return False

        result = nums[0]

        for pos in range(1, len(nums)):
            result = gcd(result, nums[pos])

        return result == 1
