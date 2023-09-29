from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        direction = A[0] <= A[-1]

        for pos in range(1, len(A)):
            if direction != (A[pos - 1] <= A[pos]) and A[pos - 1] != A[pos]:
                return False

        return True


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.isMonotonic([1])

    def test_case1(self):
        assert self.sol.isMonotonic([1, 2, 2, 3])

    def test_case2(self):
        assert self.sol.isMonotonic([6, 5, 4, 4])

    def test_case3(self):
        assert not self.sol.isMonotonic([1, 3, 2])

    def test_case4(self):
        assert self.sol.isMonotonic([1, 2, 4, 5])

    def test_case5(self):
        assert self.sol.isMonotonic([1, 1, 1])
