from typing import List
from itertools import chain


class ExamRoom:
    def __init__(self, N: int):
        self._seats = N
        self._occupied: List[int] = []

    def seat(self) -> int:
        if not self._occupied:
            self._occupied.append(0)
            return 0

        interval_len = lambda x: (x[0] + x[1] - 1) // 2 - x[0]

        max_interval = [1, 0]

        first_interval = [-self._occupied[0] + 1, self._occupied[0]]
        last_interval = [
            self._occupied[-1] + 1,
            2 * (self._seats - 1) - self._occupied[-1],
        ]

        max_interval = max(
            max_interval, first_interval, key=interval_len
        )

        for pos in range(len(self._occupied) - 1):
            interval = [self._occupied[pos] + 1, self._occupied[pos + 1]]
            max_interval = max(max_interval, interval, key=interval_len)

        max_interval = max(
            max_interval, last_interval, key=interval_len
        )

        middle = max_interval[0] + (max_interval[1] - 1 - max_interval[0]) // 2

        self._occupied.append(middle)

        for pos in reversed(range(len(self._occupied) - 1)):
            if self._occupied[pos] > self._occupied[pos + 1]:
                self._occupied[pos], self._occupied[pos + 1] = (
                    self._occupied[pos + 1],
                    self._occupied[pos],
                )

        return middle

    def leave(self, p: int) -> None:
        for pos in range(len(self._occupied)):
            if self._occupied[pos] == p:
                self._occupied[pos] = self._seats

        for pos in range(len(self._occupied) - 1):
            if self._occupied[pos] > self._occupied[pos + 1]:
                self._occupied[pos], self._occupied[pos + 1] = (
                    self._occupied[pos + 1],
                    self._occupied[pos],
                )

        self._occupied.pop()
