import heapq
from typing import List


class SeatManager:
    def __init__(self, n: int):
        self._unreserved: List[int] = list(range(1, n + 1))
        heapq.heapify(self._unreserved)

    def reserve(self) -> int:
        return heapq.heappop(self._unreserved)

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self._unreserved, seatNumber)
