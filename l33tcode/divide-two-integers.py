class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        def divide_rec(remains, sub, mul):
            while sub >= abs(divisor) and mul > 0:
                if remains - sub > 0:
                    return mul + divide_rec(remains - sub, sub << 1, mul << 1)
                elif remains - sub == 0:
                    return mul
                sub = sub >> 1
                mul = mul >> 1
            return 0

        if dividend == - (1 << 31) and divisor == -1:
            return (1 << 31) - 1

        if (dividend < 0 and divisor < 0) or (dividend > 0 and divisor > 0):
            return divide_rec(abs(dividend), abs(divisor), 1)
        else:
            return - divide_rec(abs(dividend), abs(divisor), 1)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_custom1(self):
        assert self.sol.divide(10, 3) == 3

    def test_custom2(self):
        assert self.sol.divide(7, -3) == -2

    def test_custom3(self):
        assert self.sol.divide(- 2**31, -1) == 2**31 - 1

    def test_custom4(self):
        assert self.sol.divide(-1, -1) == 1

    def test_custom4(self):
        assert self.sol.divide(-1, -1) == 1

    def test_custom5(self):
        assert self.sol.divide(1, 256) == 0

    def test_custom6(self):
        assert self.sol.divide(-1006986286, -2145851451) == 0

    def test_custom7(self):
        assert self.sol.divide(-2147483648, -3) == 715827882
