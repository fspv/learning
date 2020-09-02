from typing import List
from collections import deque


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if t == 0 and len(nums) == len(set(nums)):
            return False

        for left in range(len(nums)):
            for right in range(left + 1, min(len(nums), left + 1 + k)):
                if abs(nums[left] - nums[right]) <= t:
                    return True

        return False
