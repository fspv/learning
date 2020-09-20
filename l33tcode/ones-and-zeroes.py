from typing import List
from collections import defaultdict


class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeroes = [s.count("0") for s in strs]
        ones = [s.count("1") for s in strs]

        dp = defaultdict(int)

        dp[(0, 0)] = 0

        for pos in range(len(strs)):
            dp_new = defaultdict(int)

            for zeroes_cur, ones_cur in dp.keys():
                if zeroes_cur > m or ones_cur > n:
                    continue

                if zeroes_cur + zeroes[pos] <= m and ones_cur + ones[pos] <= n:
                    dp_new[(zeroes_cur + zeroes[pos], ones_cur + ones[pos])] = max(
                        dp[(zeroes_cur, ones_cur)] + 1,
                        dp_new[(zeroes_cur + zeroes[pos], ones_cur + ones[pos])],
                    )

                dp_new[(zeroes_cur, ones_cur)] = max(
                    dp[(zeroes_cur, ones_cur)],
                    dp_new[(zeroes_cur, ones_cur)],
                )

            dp = dp_new

        return max(dp.values())
