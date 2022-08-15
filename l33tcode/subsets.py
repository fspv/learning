from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        stack: List[int] = []
        result: List[List[int]] = []

        def dfs(pos: int) -> None:
            if pos == len(nums):
                result.append(stack.copy())
                return

            stack.append(nums[pos])
            dfs(pos + 1)
            stack.pop()
            dfs(pos + 1)

        dfs(0)

        return result

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        def sub_rec(pos, prev):
            if pos == len(nums):
                return [[]]

            result = [prev]

            for r_pos in range(pos + 1, len(nums)):
                for s in sub_rec(r_pos, prev + [nums[r_pos]]):
                    result.append(s)

            return result

        return sub_rec(-1, [])
