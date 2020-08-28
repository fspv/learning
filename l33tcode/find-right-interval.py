from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        intervals_fwd = list(sorted(range(len(intervals)), key=lambda x: intervals[x]),)
        intervals_back = list(
            sorted(
                range(len(intervals)), key=lambda x: (intervals[x][1], intervals[x][0])
            )
        )

        result = [-1] * len(intervals)
        intervals_fwd_ptr = 0
        for interval_back in intervals_back:
            while (
                intervals_fwd_ptr < len(intervals)
                and intervals[intervals_fwd[intervals_fwd_ptr]][0]
                < intervals[interval_back][1]
            ):
                intervals_fwd_ptr += 1
            if intervals_fwd_ptr == len(intervals):
                break
            result[interval_back] = intervals_fwd[intervals_fwd_ptr]

        return result
