import heapq
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Name:
    value: str

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Name):
            raise ValueError()

        return self.value < other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Name):
            raise ValueError()

        return self.value > other.value


@dataclass
class NameInversed:
    value: str

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, NameInversed):
            raise ValueError()

        return self.value > other.value

    def __gt__(self, other: object) -> bool:
        if not isinstance(other, NameInversed):
            raise ValueError()

        return self.value < other.value


class SORTracker:
    def __init__(self) -> None:
        self._left_heap: List[Tuple[int, NameInversed]] = []
        self._right_heap: List[Tuple[int, Name]] = []
        self._pos = 0

    def _inverse_string(self, name: str) -> str:
        return "".join(chr(ord("a") + ord("z") - ord(char)) for char in name)

    def _balance(self) -> None:
        if len(self._left_heap) > self._pos + 1:
            score, name_inversed = heapq.heappop(self._left_heap)

            heapq.heappush(self._right_heap, (-score, Name(name_inversed.value)))

        elif len(self._left_heap) < self._pos + 1 and self._right_heap:
            score, name = heapq.heappop(self._right_heap)

            heapq.heappush(self._left_heap, (-score, NameInversed(name.value)))

    def add(self, name: str, score: int) -> None:
        heapq.heappush(self._left_heap, (score, NameInversed(name)))

        self._balance()

    def get(self) -> str:
        _, name = self._left_heap[0]
        self._pos += 1

        self._balance()

        return name.value
