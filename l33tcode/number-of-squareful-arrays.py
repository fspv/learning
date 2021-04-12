import math
from typing import List, Set


class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        result = []

        def permutations(bitmask: int, path: List[int]) -> None:
            if len(path) == len(nums):
                result.append(path.copy())

            seen: Set[int] = set()
            for pos in range(len(nums)):
                if (
                    nums[pos] not in seen
                    and bitmask & (1 << pos) == 0
                    and (not path or math.sqrt(path[-1] + nums[pos]) % 1 == 0)
                ):
                    path.append(nums[pos])
                    permutations(bitmask | (1 << pos), path)
                    path.pop()
                    seen.add(nums[pos])

        permutations(0, [])

        return len(result)
