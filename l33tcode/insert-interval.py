from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        new_interval = newInterval

        result = []

        pos = 0

        while pos < len(intervals):
            cur_begin, cur_end = tuple(intervals[pos])
            new_begin, new_end = tuple(new_interval)

            if cur_end < new_begin:
                result.append(intervals[pos])
            elif new_end < cur_begin:
                break
            else:
                new_interval = [min(new_begin, cur_begin), max(new_end, cur_end)]

            pos += 1

        result.append(new_interval)
        result += intervals[pos:]

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.insert([], [1, 2]) == [[1, 2]]

    def test_case1(self):
        assert self.sol.insert([[1, 3], [6, 9]], [2, 5]) == [[1, 5], [6, 9]]

    def test_case2(self):
        assert self.sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]) == [
            [1, 2],
            [3, 10],
            [12, 16],
        ]

    def test_case3(self):
        assert self.sol.insert([[1, 3], [6, 9]], [-1, 0]) == [[-1, 0], [1, 3], [6, 9]]

    def test_case4(self):
        assert self.sol.insert([[1, 3], [6, 9]], [50, 100]) == [
            [1, 3],
            [6, 9],
            [50, 100],
        ]
