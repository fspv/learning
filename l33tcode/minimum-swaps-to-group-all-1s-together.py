from typing import List


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = data.count(1)

        zeroes = data[:ones].count(0)

        min_swaps = len(data)

        for right in range(ones, len(data)):
            min_swaps = min(min_swaps, zeroes)

            zeroes += 1 - data[right]
            zeroes -= 1 - data[right - ones]

        min_swaps = min(min_swaps, zeroes)

        return min_swaps
