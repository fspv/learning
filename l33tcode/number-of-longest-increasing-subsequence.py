from typing import List
from functools import lru_cache


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        max_length = 0
        max_length_count = len(nums)

        lengths = [0] * len(nums)
        ways = [1] * len(nums)

        for start in range(len(nums)):
            for end in range(start + 1, len(nums)):
                if nums[start] < nums[end]:
                    new_length = lengths[start] + 1

                    if lengths[end] < new_length:
                        lengths[end] = new_length
                        ways[end] = ways[start]
                    elif lengths[end] == new_length:
                        ways[end] += ways[start]

                    if max_length < new_length:
                        max_length = new_length
                        max_length_count = ways[start]
                    elif max_length == new_length:
                        max_length_count += ways[start]

        return max_length_count
