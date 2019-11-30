from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], to_be_removed: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            for new_int in [
                [interval[0], min(to_be_removed[0], interval[1])],
                [max(to_be_removed[1], interval[0]), interval[1]]
            ]:
                if new_int[0] < new_int[1]:
                    result.append(new_int)

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.removeInterval([[0,2],[3,4],[5,7]], [1,6]) == [[0,1],[6,7]]

    def test_case2(self):
        assert self.sol.removeInterval([[0,5]], [2,3]) == [[0,2],[3,5]]

    def test_case3(self):
        assert self.sol.removeInterval([[0,5]], [2,2]) == [[0,2],[2,5]]

    def test_case4(self):
        assert self.sol.removeInterval([], []) == []

    def test_case5(self):
        assert self.sol.removeInterval([[0,100]], [0,50]) == [[50,100]]
