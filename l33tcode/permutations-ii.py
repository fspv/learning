from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []

        def permutations(bitmask: int, path: List[int]) -> int:
            if len(path) == len(nums):
                result.append(path.copy())

            seen = set()
            for pos in range(len(nums)):
                if nums[pos] not in seen and bitmask & (1 << pos) == 0:
                    path.append(nums[pos])
                    permutations(bitmask | (1 << pos), path)
                    path.pop()
                    seen.add(nums[pos])

        permutations(0, [])

        return result
