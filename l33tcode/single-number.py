from collections import Counter
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return next(k for k, v in Counter(nums).items() if v == 1)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.singleNumber([2, 2, 1]) == 1

    def test_case2(self):
        assert self.sol.singleNumber([4, 1, 2, 1, 2]) == 4
