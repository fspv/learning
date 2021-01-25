from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        one = -1

        for pos in range(len(nums)):
            if nums[pos] == 1:
                if one >= 0 and pos - one - 1 < k:
                    return False
                one = pos

        return True
