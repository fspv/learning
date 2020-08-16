from typing import List, Tuple
from functools import lru_cache


class Solution:
    @staticmethod
    def _suffix_sum(piles: List[int]) -> List[int]:
        suffix_sum = [0]

        for pile in reversed(piles):
            suffix_sum.append(suffix_sum[-1] + pile)

        suffix_sum.reverse()

        return suffix_sum

    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        dp = [[0] * (len(piles) + 1) for _ in range(len(piles) + 1)]

        for pile in reversed(range(len(piles))):
            for M in reversed(range(len(piles))):
                sum_next_player = suffix_sum[pile]

                for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                    sum_next_player = min(
                        sum_next_player, dp[next_pile][max(M, next_pile - pile)]
                    )

                sum_player = suffix_sum[pile] - sum_next_player

                dp[pile][M] = sum_player

        return dp[0][1]

    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        @lru_cache(None)
        def dfs(pile: int, M: int) -> int:
            sum_next_player = suffix_sum[pile]

            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_next_player = min(
                    sum_next_player, dfs(next_pile, max(M, next_pile - pile))
                )

            sum_player = suffix_sum[pile] - sum_next_player

            return sum_player

        return dfs(0, 1)

    def stoneGameII(self, piles: List[int]) -> int:
        suffix_sum = self._suffix_sum(piles)

        @lru_cache(None)
        def dfs(pile: int, M: int, turn: bool) -> Tuple[int, int]:
            # turn: true - alex, false - lee
            sum_alex, sum_lee = suffix_sum[pile], suffix_sum[pile]

            for next_pile in range(pile + 1, min(pile + 2 * M + 1, len(piles) + 1)):
                sum_alex_next, sum_lee_next = dfs(
                    next_pile, max(M, next_pile - pile), not turn
                )
                range_sum = suffix_sum[pile] - suffix_sum[next_pile]

                if turn:
                    if sum_lee_next < sum_lee:
                        sum_alex = sum_alex_next + range_sum
                        sum_lee = sum_lee_next
                else:
                    if sum_alex_next < sum_alex:
                        sum_alex = sum_alex_next
                        sum_lee = sum_lee_next + range_sum

            return sum_alex, sum_lee

        return dfs(0, 1, True)[0]
