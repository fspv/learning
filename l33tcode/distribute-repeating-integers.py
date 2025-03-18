from typing import List
from collections import Counter


class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        def backtrack(piles: List[int], customer: int) -> bool:
            if customer == len(quantity):
                return True

            for pile in range(len(piles)):
                if piles[pile] >= quantity[customer]:
                    piles[pile] -= quantity[customer]
                    if backtrack(piles, customer + 1):
                        return True
                    piles[pile] += quantity[customer]

            return False

        piles = list(Counter(nums).values())
        piles.sort(reverse=True)
        quantity.sort(reverse=True)
        return backtrack(piles, 0)
