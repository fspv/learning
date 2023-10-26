from typing import List
from functools import cache
from bisect import bisect_left


MOD = 10 ** 9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        num_sorted = sorted(set(arr), reverse=True)

        @cache
        def dp(pos: int) -> int:
            trees = 1

            for left in range(pos, len(num_sorted)):
                div = num_sorted[pos] / num_sorted[left]

                if div > num_sorted[left]:
                    continue

                right = bisect_left(
                    num_sorted,
                    -div,
                    pos,
                    len(num_sorted),
                    key=lambda x: -x,
                )

                if (
                    right < len(num_sorted)
                    and num_sorted[right] * num_sorted[left] == num_sorted[pos]
                ):
                    trees += (dp(left) * dp(right) * (2 - (left == right))) % MOD

            return trees % MOD

        return sum([dp(pos) for pos in range(len(num_sorted))]) % MOD
