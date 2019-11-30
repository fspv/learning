from typing import List
from itertools import chain


class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        dp, prev = [float("+inf")] * len(S), float("-inf")

        for pos in chain(range(len(S)), reversed(range(len(S)))):
            prev = pos if S[pos] == C else prev

            dp[pos] = min(abs(pos - prev), dp[pos])

        return dp


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.shortestToChar("x", "x") == [0]

    def test_case1(self):
        assert self.sol.shortestToChar("loveleetcode", "e") == [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
