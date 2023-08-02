from typing import List, Set


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        nums_set: Set[int] = set(nums)
        stack: List[int] = []
        result: List[List[int]] = []

        def permutations():
            if not nums_set:
                result.append(stack.copy())
                return

            for num in list(nums_set):
                nums_set.discard(num)
                stack.append(num)
                permutations()
                nums_set.add(num)
                stack.pop()

        permutations()

        return result
