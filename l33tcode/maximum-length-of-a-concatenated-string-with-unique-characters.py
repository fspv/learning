from typing import List
from itertools import combinations


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        tmp_set = set()
        tmp_dict = {}

        def dfs(pos):
            if pos < len(arr):
                for c in arr[pos]:
                    if c in tmp_set:
                        dfs(pos + 1)
                        

        return max_len


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.maxLength(["un","iq","ue"]) == 4

    def test_case2(self):
        assert self.sol.maxLength(["cha","r","act","ers"]) == 6

    def test_case3(self):
        assert self.sol.maxLength(["abcdefghijklmnopqrstuvwxyz"]) == 26

    def test_case4(self):
        assert self.sol.maxLength(["un","iq","ue", "xy"]) == 6
