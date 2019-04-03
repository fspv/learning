import unittest

class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 0]

        for pos in reversed(range(len(s))):
            ways = 0

            if int(s[pos]) > 0:
                ways += dp[0] if int(s[pos]) < 27 else 0
                ways += dp[1] if int(s[pos:(pos + 2)]) < 27 else 0

            dp = [ways, dp[0]]

        return dp[0] if len(s) else 0


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.numDecodings(""), 0)

    def test_one1(self):
        self.assertEqual(self.sol.numDecodings("1"), 1)

    def test_one0(self):
        self.assertEqual(self.sol.numDecodings("0"), 0)

    def test_two1(self):
        self.assertEqual(self.sol.numDecodings("12"), 2)

    def test_two2(self):
        self.assertEqual(self.sol.numDecodings("01"), 0)

    def test_custom1(self):
        self.assertEqual(self.sol.numDecodings("226"), 3)

    def test_custom2(self):
        self.assertEqual(self.sol.numDecodings("2281337"), 4)

    def test_custom3(self):
        self.assertEqual(self.sol.numDecodings("2280337"), 0)

    def test_custom3(self):
        self.assertEqual(self.sol.numDecodings("2210337"), 2)


if __name__ == "__main__":
    unittest.main()
