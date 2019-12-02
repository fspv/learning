import math


class Solution:
    def arrangeCoins(self, n: int) -> int:
        # sum = n * (n + 1) / 2
        # n^2 + n - 2 * sum = 0
        # n^2 + 2 * (1/2) * n + 1/4 - 1/4 - 2 * sum = 0
        # (n + 1/2)^2 = 1/4 + 2 * sum
        # n = sqrt(1/4 + 2 * sum) - 1/2
        return int(math.sqrt(1 / 4 + 2 * n) - 1 / 2)
