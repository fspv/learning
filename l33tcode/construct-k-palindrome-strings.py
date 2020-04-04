from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        odd = len([0 for c in Counter(s).values() if c % 2])

        return k >= odd and k > 0 and k <= len(s)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.canConstruct("annabelle", 2)

    def test_case2(self):
        assert not self.sol.canConstruct("leetcode", 3)

    def test_case3(self):
        assert self.sol.canConstruct("true", 4)

    def test_case4(self):
        assert self.sol.canConstruct("yzyzyzyzyzyzyzy", 2)

    def test_case5(self):
        assert not self.sol.canConstruct("cr", 7)

    def test_case6(self):
        assert not self.sol.canConstruct("", 7)

    def test_case7(self):
        assert self.sol.canConstruct("a", 1)

    def test_case8(self):
        assert not self.sol.canConstruct("a", 0)
