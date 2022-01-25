from dataclasses import dataclass
from typing import List, Tuple


# Definition for an Interval.
@dataclass
class Interval:
    start: int
    end: int


class Solution:
    def employeeFreeTime(self, schedule: List[List[Interval]]) -> List[Interval]:
        points: List[Tuple[int, int]] = []

        # Interval starts - increase the number of intervals starting from here
        # Interval ends - decrease the number of intervals starting from here
        for intervals in schedule:
            for interval in intervals:
                points.append((interval.start, 1))
                points.append((interval.end, -1))

        # Sort all the points, so we can tell how many intervals exist in any
        # particular point
        points.sort()

        free_times: List[Interval] = []
        start = -1
        count = 0

        # Go over all points, keeping track on places where there are no
        # intervals exist anymore
        for position, adj in points:
            count += adj

            if count == 0:
                # Start of the free interval
                if start == -1:
                    start = position
            else:
                # Reset start, as this point is not a valid start anymore
                if start == position:
                    start = -1

                # Start has been set before, free interval is over, add it to
                # the answer
                if start != -1:
                    free_times.append(Interval(start, position))
                    start = -1

        return free_times
