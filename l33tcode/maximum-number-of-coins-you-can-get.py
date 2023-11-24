from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()

        left, right = 0, len(piles) - 2

        result = 0

        while left < right:
            result += piles[right]
            left += 1
            right -= 2

        return result
