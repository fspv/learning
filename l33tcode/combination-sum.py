from functools import lru_cache

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

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
