import math


class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A) < 3:
            return 0

        count = 2
        diff = A[1] - A[0]

        result = 0
        comb = lambda n: math.factorial(n) // math.factorial(n - 2) // 2

        for pos in range(2, len(A)):
            if A[pos] - A[pos - 1] == diff:
                count += 1
            else:
                if count > 1:
                    result += comb(count) - (count - 1)
                diff = A[pos] - A[pos - 1]
                count = 2

        if count > 1:
            result += comb(count) - (count - 1)

        return result
