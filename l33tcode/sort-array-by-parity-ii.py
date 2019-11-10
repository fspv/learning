from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        idx = 1

        for pos in range(0, len(A), 2):
            if A[pos] % 2 == 0:
                continue

            while A[idx] % 2 != 0:
                idx += 2

            A[pos], A[idx] = A[idx], A[pos]

        return A


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.sortArrayByParityII([]) == []

    def test_case1(self):
        assert self.sol.sortArrayByParityII([1,2]) == [2,1]

    def test_case2(self):
        assert self.sol.sortArrayByParityII([4,2,5,7]) == [4,5,2,7]

    def test_case3(self):
        assert self.sol.sortArrayByParityII([1] * 10000 + [2] * 10000) == [2,1] * 10000

    def test_case4(self):
        for _ in range(100):
            assert self.sol.sortArrayByParityII([2] * 10000 + [1] * 10000) == [2,1] * 10000
