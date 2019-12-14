from typing import List


class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        for row in range(1, len(arr)):
            for col in range(len(arr[0])):
                left = arr[row - 1][:col]
                right = arr[row - 1][col + 1:]
                arr[row][col] += min(left + right)

        return min(arr[-1])


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.minFallingPathSum([[1,2,3],[4,5,6],[7,8,9]]) == 13

    def test_case2(self):
        assert self.sol.minFallingPathSum([[9]]) == 9

    def test_case3(self):
        assert self.sol.minFallingPathSum([[-1000,2,3],[4,5,6],[7,8,9]]) == -988

    def test_case4(self):
        assert self.sol.minFallingPathSum([[1,2,-1000],[4,5,6],[7,8,9]]) == -988

    def test_case5(self):
        assert self.sol.minFallingPathSum(
            [
                [-73,61,43,-48,-36],
                [3,  30,27, 57, 10],
                [96,-76,84, 59,-15],
                [5, -49,76, 31, -7],
                [97, 91,61,-46, 67]
            ]
        ) == - 192

    def test_case6(self):
        assert self.sol.minFallingPathSum(
            [
                [-37,51,-36,34,-22],
                [ 82, 4,  30,14, 38],
                [-68,-52,-92,65,-85],
                [-49,-3, -77, 8,-19],
                [-60,-71,-21,-62,-73]
            ]
        ) == -268

    def test_case7(self):
        assert self.sol.minFallingPathSum(
            [
                [-73,61,43,-48,-36],
                [3,  30,27, 57, 10],
                [96,-76,84, 59,-15],
                [5, -49,76, 31, -7],
                [97, 91,61,-46, 67]
            ]
        ) == - 192
