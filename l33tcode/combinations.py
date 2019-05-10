class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def combinations(pos, kk):
            if pos + kk > n + 1:
                return []

            if kk == 0:
                return [[]]

            result = []
            for r_pos in range(pos, n + 1):
                for comb in combinations(r_pos + 1, kk - 1):
                    result.append([r_pos] + comb)

            return result

        return combinations(1, k)
