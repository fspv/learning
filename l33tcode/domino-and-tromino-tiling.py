from functools import lru_cache


class Solution:
    def numTilings(self, N: int) -> int:
        MOD = 10 ** 9 + 7

        @lru_cache(None)
        def backtrack(row1: int, row2: int, col: int) -> int:
            if col > N:
                return 0

            if col == N:
                if row1 == row2:
                    return 1
                return 0

            ways = 0

            if row1 == 1 and row2 == 0:
                ways += backtrack(row1 % 2, (row2 + 2) % 2, col + 1)
                ways += backtrack((row1 + 1) % 2, (row2 + 2) % 2, col + 2)
            elif row1 == 0 and row2 == 1:
                ways += backtrack((row1 + 2) % 2, (row2) % 2, col + 1)
                ways += backtrack((row1 + 2) % 2, (row2 + 1) % 2, col + 2)
            else:
                ways += backtrack((row1 + 2) % 2, (row2 + 2) % 2, col + 2)
                ways += backtrack((row1 + 1) % 2, (row2 + 1) % 2, col + 1)
                ways += backtrack((row1 + 1) % 2, (row2 + 2) % 2, col + 1)
                ways += backtrack((row1 + 2) % 2, (row2 + 1) % 2, col + 1)

            return ways % MOD

        return backtrack(0, 0, 0)
