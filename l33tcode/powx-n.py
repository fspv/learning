class Solution:
    def myPow(self, x, n):
        def power(x, n):
            if n == 1:
                return x
            elif n == 0:
                return 1
            else:
                return power(x * x, n // 2) * power(x, n % 2)

        if n >= 0:
            return power(x, n)
        elif n < 0:
            return 1 / power(x, -n)

    def myPowIterative(self, x: float, n: int) -> float:
        result = 1.0

        num = x
        pow = 1

        # Using the property that each number can
        # be represented as a sum of powers of 2
        while pow <= abs(n):
            result *= num if abs(n) & pow else 1

            num *= num
            pow <<= 1

        return result if n >= 0 else 1 / result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_zero1(self):
        assert self.sol.myPow(0, 0) == 1

    def test_zero2(self):
        assert self.sol.myPow(0, 1) == 0

    def test_zero3(self):
        assert self.sol.myPow(0, 2) == 0

    def test_one1(self):
        assert self.sol.myPow(1, 0) == 1

    def test_one2(self):
        assert self.sol.myPow(1, 1) == 1

    def test_one3(self):
        assert self.sol.myPow(1, 4) == 1

    def test_custom1(self):
        assert self.sol.myPow(2, 10) == 1024

    def test_custom2(self):
        assert self.sol.myPow(2.1, 3) == 9.261000000000001

    def test_custom3(self):
        assert self.sol.myPow(2, -2) == 0.25

    def test_custom4(self):
        assert self.sol.myPow(2, 11) == 2048
