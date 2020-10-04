from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0
        prev_interval = [float("-inf")] * 2

        for interval in intervals:
            if interval[1] > prev_interval[1]:
                count += 1
                prev_interval = interval

        return count


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.removeCoveredIntervals([[1,4],[3,6],[2,8]]) == 2

    def test_case2(self):
        assert self.sol.removeCoveredIntervals([[1, 2]]) == 1

    def test_case3(self):
        assert self.sol.removeCoveredIntervals([[66672,75156],[59890,65654],[92950,95965],[9103,31953],[54869,69855],[33272,92693],[52631,65356],[43332,89722],[4218,57729],[20993,92876]]) == 3
