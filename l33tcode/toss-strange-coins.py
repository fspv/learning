from typing import List
from functools import lru_cache


class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        @lru_cache(None)
        def dp(coin: int, value: int) -> float:
            if coin == len(prob):
                return int(value == 0)

            return (
                ((dp(coin + 1, value - 1) * prob[coin]) if value > 0 else 0)
                + dp(coin + 1, value) * (1 - prob[coin])
            )

        return dp(0, target)
