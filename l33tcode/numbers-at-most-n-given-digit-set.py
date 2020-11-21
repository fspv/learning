import math
from typing import List


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        num = list(map(int, str(n)))

        result = 0

        for length in range(1, len(num)):
            result += len(digits) ** length

        def dfs(pos: int) -> int:
            if pos == len(num):
                return 1

            combinations = 0

            for digit in map(int, digits):
                if digit < int(num[pos]):
                    combinations += len(digits) ** (len(num) - (pos + 1))
                elif digit == int(num[pos]):
                    combinations += dfs(pos + 1)

            return combinations

        return dfs(0) + result
