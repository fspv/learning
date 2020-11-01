import math


class Solution:
    def countVowelStrings(self, count: int) -> int:
        def comb(n: int, k: int) -> int:
            return math.factorial(n) // math.factorial(n - k) // math.factorial(k)

        return comb(count + 4, count)
