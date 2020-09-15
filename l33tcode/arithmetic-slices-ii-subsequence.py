from typing import Optional, List
from functools import lru_cache
from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [{} for _ in A]

        count = 0

        for pos in range(len(A)):
            for prev_pos in range(pos):
                diff = A[pos] - A[prev_pos]

                dp[pos][diff] = dp[pos].get(diff, 0)

                dp[pos][diff] += dp[prev_pos].get(diff, 0) + 1
                count += dp[prev_pos].get(diff, 0)

        return count

    def numberOfArithmeticSlicesTopDown(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs(pos: int, prev_pos: int, diff: int, flag: bool) -> int:
            if pos == len(A):
                return int(flag)

            count = 0

            for prev_pos in range(pos):
                if diff:
                    if A[pos] - A[prev_pos] == diff:
                        dfs(pos + 1, diff, True)
                else:
                    dfs(pos + 1, diff, False)

            if prev_pos == -1:
                count += dfs(pos + 1, pos, None, False)
            elif diff is None:
                count += dfs(pos + 1, pos, A[pos] - A[prev_pos], False)
            elif A[pos] - A[prev_pos] == diff:
                count += dfs(pos + 1, pos, diff, True)

            count += dfs(pos + 1, prev_pos, diff, flag)

            return count

        return dfs(0, -1, None, False)
