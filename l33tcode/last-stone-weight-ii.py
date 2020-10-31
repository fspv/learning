from typing import List, Union
from functools import lru_cache


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)

        @lru_cache(None)
        def dp(pos: int, agg: int) -> Union[float, int]:
            nonlocal total

            if pos == len(stones):
                return 0

            max_weight = 0

            if agg >= stones[pos]:
                max_weight = max(
                    max_weight, dp(pos + 1, agg - stones[pos]) + stones[pos]
                )

            max_weight = max(max_weight, dp(pos + 1, agg))

            return max_weight

        return total - 2 * int(dp(0, total // 2))

    def lastStoneWeightIIBruteForce(self, stones: List[int]) -> int:
        def dp(stone_bitmap: int) -> int:
            max_weight = float("+inf")
            count = 0
            for left in range(len(stones)):
                for right in range(left + 1, len(stones)):
                    if stone_bitmap & (1 << left | 1 << right) == 0:
                        smashed_weight = (
                            stones[left]
                            + stones[right]
                            - min(stones[left], stones[right]) * 2
                        )
                        if smashed_weight == 0:
                            max_weight = min(
                                max_weight, dp(stone_bitmap | (1 << left | 1 << right))
                            )
                        else:
                            tmp = stones[left]
                            stones[left] = smashed_weight
                            max_weight = min(max_weight, dp(stone_bitmap | 1 << right))
                            stones[left] = tmp
                        count += 1

            if count == 0:
                pos = 0
                while stone_bitmap & (1 << pos) > 0:
                    pos += 1

                max_weight = stones[pos]

            return max_weight

        return dp(0)
