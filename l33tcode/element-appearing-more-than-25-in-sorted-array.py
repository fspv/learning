from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quarter = len(arr) // 4

        cur_len = 0
        cur_num = None

        for num in arr:
            if num == cur_num:
                cur_len += 1
            else:
                cur_len = 1

            cur_num = num

            if cur_len > quarter:
                return num


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.findSpecialInteger([10]) == 10

    def test_case2(self):
        assert self.sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]) == 6

    def test_case3(self):
        assert self.sol.findSpecialInteger([1,1,2,2,3,3,4,4]) is None

    def test_case4(self):
        assert self.sol.findSpecialInteger([1,1,1,2,3,3,4,4]) == 1
