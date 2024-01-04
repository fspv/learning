from typing import Counter, List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        counts = Counter(nums)

        ops = 0

        for count in counts.values():
            if count == 1:
                return -1

            ops += count // 3

            if count % 3 != 0:
                ops += 1

        return ops
