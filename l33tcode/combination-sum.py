from functools import lru_cache
from typing import List


class Solution:
    def combinationSum1(self, candidates: List[int], target: int) -> List[List[int]]:
        @lru_cache(None)
        def com_sum_rec(remain, pos):
            if remain == 0:
                return [[]]

            if remain < 0:
                return []

            result = []

            for cand_pos in range(pos, len(candidates)):
                for cont in com_sum_rec(remain - candidates[cand_pos], cand_pos):
                    result.append([candidates[cand_pos]] + cont)

            return result

        return com_sum_rec(target, 0)

    def combinationSum(
        self, candidates: List[int], init_target: int
    ) -> List[List[int]]:
        stack: List[int] = []
        result: List[List[int]] = []

        def dfs(candidate: int, target: int) -> None:
            if target == 0:
                result.append(stack.copy())
                return

            if target < 0:
                return

            if candidate == len(candidates):
                return

            times = 1
            while target - candidates[candidate] * times >= 0:
                stack.append(candidates[candidate])
                dfs(candidate + 1, target - candidates[candidate] * times)
                times += 1

            for _ in range(times - 1):
                stack.pop()

            dfs(candidate + 1, target)

        dfs(0, init_target)

        return result
