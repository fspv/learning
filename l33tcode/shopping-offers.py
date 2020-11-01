from typing import List, Tuple
from functools import lru_cache


class Solution:
    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        offers = {}

        for pos in range(len(special)):
            offer = tuple(special[pos][:-1])
            offers[offer] = min(offers.get(tuple(offer), float("+inf")), special[pos][-1])

        @lru_cache(None)
        def dp(left: Tuple[int]) -> int:
            if all(l == 0 for l in left):
                return 0

            if any(l < 0 for l in left):
                return float("+inf")

            if offer == len(special):
                return float("+inf")

            min_price = sum(left[pos] * price[pos] for pos in range(len(left)))
            for zhopa, zhopa3 in offers.items():
                zhopa2 = tuple(map(lambda x: x[0] - x[1], zip(left, zhopa)))
                min_price = min(
                    min_price,
                    dp(zhopa2) + zhopa3,
                )

            return min_price

        return dp(tuple(needs))
