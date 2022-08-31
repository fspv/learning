from typing import List, Tuple

from sortedcontainers import SortedList


class CountIntervals:
    def __init__(self) -> None:
        self._intervals: SortedList[Tuple[int, int]] = SortedList()
        self._count = 0

    def add(self, left: int, right: int) -> None:
        new_start, new_end = left, right

        to_delete: List[Tuple[int, int]] = []

        # Merge all the intervals, intersecting with this one
        for start, end in self._intervals.islice(
            start=max(0, self._intervals.bisect_left((left, 0)) - 1)
        ):
            if end < left:
                continue

            if start > right:
                break

            if right <= end:
                new_end = end

            if left >= start:
                new_start = start

            self._count -= min(end, right) - max(start, left) + 1

            to_delete.append((start, end))

        # Remove merged intervals from the list
        for start, end in to_delete:
            self._intervals.remove(value=(start, end))

        # Add the new merged intervals
        self._intervals.add((new_start, new_end))
        self._count += right - left + 1

    def count(self) -> int:
        return self._count


# Your CountIntervals object will be instantiated and called as such:
# obj = CountIntervals()
# obj.add(left,right)
# param_2 = obj.count()
