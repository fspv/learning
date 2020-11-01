import math


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        comb = lambda n, k: math.factorial(n) // math.factorial(n - k) // math.factorial(k)
        perm = lambda n, k: math.factorial(n) // math.factorial(n - k)

        result = 1
        for digits in range(1, n + 1):
            result += perm(10, digits) - perm(9, digits - 1)

        return result
