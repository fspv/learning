from typing import List, Set


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()

        seen: Set[int] = set()

        ops = 0

        for num in nums:
            seen.add(num)

            ops += len(seen) - 1

        return ops
