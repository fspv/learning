class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n < 3:
            return 1

        first, second, third = 0, 1, 1

        for _ in range(2, n):
            first, second, third = second, third, first + second + third

        return third
