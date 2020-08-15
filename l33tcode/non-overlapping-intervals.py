from typing import List


class Interval:
    def __init__(self, begin: float, end: float) -> None:
        self.begin = begin
        self.end = end

    def overlaps(self, other: "Interval") -> bool:
        if self.begin <= other.begin < self.end:
            return True

        if self.begin < other.end <= self.end:
            return True

        return False


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev_begin, prev_end = float("-inf"), float("-inf")

        skipped = 0
        for interval in intervals:
            if interval[0] >= prev_end:
                prev_end = interval[1]
            elif interval[1] <= prev_end:
                prev_end = interval[1]
                skipped += 1
            else:
                skipped += 1

        return skipped

    def eraseOverlapIntervalsDP2(self, intervals: List[List[int]]) -> int:
        intervals_obj = [Interval(float("-inf"), float("-inf"))] + list(
            map(lambda x: Interval(float(x[0]), float(x[1])), intervals)
        )

        intervals_obj.sort(key=lambda x: (x.end, x.begin))
        dp = [float("+inf")] * (len(intervals_obj))
        dp[0] = 0

        for interval in range(1, len(intervals_obj)):
            interval_obj = intervals_obj[interval]
            dp[interval] =  dp[interval - 1] + 1

            for prev_interval in reversed(range(0, interval)):
                prev_interval_obj = intervals_obj[prev_interval]
                distance = interval - prev_interval - 1

                if not interval_obj.overlaps(prev_interval_obj):
                    dp[interval] = min(
                        dp[interval], dp[prev_interval] + distance
                    )
                    break

        return int(dp[-1])

    def eraseOverlapIntervalsDP1(self, intervals: List[List[int]]) -> int:
        dp = [float("+inf")] * (len(intervals) + 1)
        dp[0] = 0

        intervals.sort()

        for interval in range(len(intervals)):
            for prev_interval in range(-1, interval):
                distance = interval - prev_interval - 1
                if distance > dp[interval + 1]:
                    break

                begin, end = intervals[interval]

                prev_begin, prev_end = float("-inf"), float("-inf")
                if prev_interval >= 0:
                    prev_begin, prev_end = intervals[prev_interval]

                dp[interval + 1] = min(
                    dp[interval + 1],
                    dp[prev_interval + 1] + distance + 1,
                    dp[prev_interval + 1] + distance
                    if begin >= prev_end
                    else float("+inf"),
                )

        return dp[-1]

    def eraseOverlapIntervalsTopDown(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        def dfs(interval: int, prev_interval: int) -> int:
            if interval == len(intervals):
                return 0

            begin, end = intervals[interval]
            prev_begin, prev_end = float("-inf"), float("-inf")
            if prev_interval >= 0:
                prev_begin, prev_end = intervals[prev_interval]

            return min(
                dfs(interval + 1, prev_interval) + 1,
                dfs(interval + 1, interval) if begin >= prev_end else float("+inf"),
            )

        return dfs(0, -1)
