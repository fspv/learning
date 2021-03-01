from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_types = set(candyType)

        return min(len(candyType) // 2, len(candy_types))
