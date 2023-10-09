from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        @cache
        def dp(pos1: int, pos2: int) -> int:
            if pos1 == len(nums1) or pos2 == len(nums2):
                return 0

            # Take both and ignore the rest (otherwise we'll have to pick
            # something else, which might be not optimal)
            max_product = nums1[pos1] * nums2[pos2]
            # Take both
            max_product = max(
                max_product, dp(pos1 + 1, pos2 + 1) + nums1[pos1] * nums2[pos2]
            )
            # Skip first
            if pos1 + 1 < len(nums1):
                max_product = max(max_product, dp(pos1 + 1, pos2))
            # Skip second
            if pos2 + 1 < len(nums2):
                max_product = max(max_product, dp(pos1, pos2 + 1))

            return max_product

        return dp(0, 0)
