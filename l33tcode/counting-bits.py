class Solution:
    def countBits(self, num):
        if num == 0:
            return [0]

        dp = [0] * (num + 1)
        power = 1

        for pos in range(1, num + 1):
            if pos == power * 2:
                power = power * 2

            dp[pos] = dp[pos - power] + 1

        return dp

class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_zero(self):
        assert self.sol.countBits(0) == [0]

    def test_one(self):
        assert self.sol.countBits(1) == [0, 1]

    def test_two(self):
        assert self.sol.countBits(2) == [0, 1, 1]

    def test_five(self):
        assert self.sol.countBits(5) == [0, 1, 1, 2, 1, 2]

    def test_eight(self):
        assert self.sol.countBits(8) == [0, 1, 1, 2, 1, 2, 2, 3, 1]
