from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        for pos in range(1, len(prices)):
            if (diff := prices[pos] - prices[pos - 1]) > 0:
                result += diff
        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.maxProfit([7, 1, 5, 3, 6, 4]) == 7

    def test_case2(self):
        assert self.sol.maxProfit([1, 2, 3, 4, 5]) == 4

    def test_case3(self):
        assert self.sol.maxProfit([7, 6, 4, 3, 1]) == 0

    def test_case4(self):
        assert self.sol.maxProfit([]) == 0
