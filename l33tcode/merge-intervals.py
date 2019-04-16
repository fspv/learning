import unittest

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other.start and self.end == other.end


class Solution(object):
    def merge(self, intervals):
        intervals.sort(key=lambda x: x.start)

        result = []

        if len(intervals):
            result.append(intervals[0])

        for interval in intervals:
            if result[-1].end >= interval.start:
                if result[-1].end < interval.end:
                    result[-1].end = interval.end
            else:
                result.append(interval)

        return result

    def merge2(self, intervals: List[List[int]]) -> List[List[int]]:
        # Shorter version, less LOC and new input
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        result = []

        for interval in sorted_intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append([interval[0], interval[1]])

        return result


class TestSolution(unittest.TestCase):
    def test_merge(self):
        sol = Solution()

        self.assertListEqual(sol.merge([]), [])
        self.assertListEqual(sol.merge([Interval(0, 0)]), [Interval(0, 0)])
        self.assertListEqual(
            sol.merge([Interval(1, 10), Interval(3, 10)]),
            [Interval(1, 10)]
        )
        self.assertListEqual(
            sol.merge([Interval(1, 10), Interval(0, 0)]),
            [Interval(0, 0), Interval(1, 10)]
        )
        self.assertListEqual(
            sol.merge([Interval(1, 11), Interval(3, 10)]),
            [Interval(1, 11)]
        )
        self.assertListEqual(
            sol.merge([Interval(1, 10), Interval(0, 10)]),
            [Interval(0, 10)]
        )
        self.assertListEqual(
            sol.merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]),
            [Interval(1, 6), Interval(8, 10), Interval(15, 18)]
        )
        self.assertListEqual(sol.merge([Interval(1, 4), Interval(4, 5)]), [Interval(1, 5)])
