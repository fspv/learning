from typing import List
from collections import Counter


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)

        return list(sorted(nums, key=lambda num: (counter[num], -num)))
