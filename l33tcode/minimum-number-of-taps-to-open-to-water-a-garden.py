from functools import cache
from typing import List, Tuple


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = n + 1

        intervals: List[Tuple[int, int]] = []

        for tap in range(taps):
            intervals.append((tap - ranges[tap], tap + ranges[tap]))

        intervals.sort()

        # Dummy interval outside the garden
        intervals.append((n, n + 1))

        @cache
        def dp(interval: int) -> int:
            if interval == taps:
                # Hit the final dummy interval
                return 0

            min_taps = taps + 1

            for next_interval in range(interval + 1, len(intervals)):
                if intervals[interval][1] >= intervals[next_interval][0]:
                    # Take
                    min_taps = min(min_taps, dp(next_interval) + 1)
                else:
                    # Skip this and everything after, as there is no overlap
                    break

            return min_taps

        min_taps = taps + 1
        for interval in range(taps):
            if intervals[interval][0] <= 0:
                min_taps = min(min_taps, dp(interval))

        return min_taps if min_taps < taps + 1 else -1
