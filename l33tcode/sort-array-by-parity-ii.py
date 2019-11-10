from typing import List


class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        idx = [0, 0]  # [even_idx, odd_idx]

        even = True

        for pos in range(len(A)):
            rem = 0 if even else 1

            while A[idx[rem]] % 2 != rem:
                idx[rem] += 1

            A[pos], A[idx[rem]] = A[idx[rem]], A[pos]

            idx[rem] += 1
            even = not even

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
