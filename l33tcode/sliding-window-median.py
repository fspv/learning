import heapq
from typing import List, Tuple, Set


class WindowHeap:
    def __init__(self, window_size: int, min_heap: bool) -> None:
        self.heap: List[Tuple[int, int]] = []
        self.present: Set[Tuple[int, int]] = set()
        self.min_heap = min_heap

    def push(self, value: int, pos: int) -> None:
        if self.min_heap:
            item = (value, pos)
        else:
            item = (-value, pos)
        heapq.heappush(self.heap, item)
        self.present.add(item)

    def pop(self) -> Tuple[int, int]:
        self[0]  # get item to clean up discarded

        value, pos = heapq.heappop(self.heap)
        self.present.discard((value, pos))

        if not self.min_heap:
            value = -value

        return value, pos

    def discard(self, value: int, pos: int) -> None:
        if self.min_heap:
            self.present.discard((value, pos))
        else:
            self.present.discard((-value, pos))

    def __len__(self) -> int:
        return len(self.present)

    def __getitem__(self, key: int) -> int:
        while self.heap[0] not in self.present:
            value, pos = heapq.heappop(self.heap)
            continue

        value, pos = self.heap[0]

        if not self.min_heap:
            value = -value

        return value


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        def median(heap_left: List[int], heap_right: List[int]) -> float:
            raise NotImplementedError()

        heap_left, heap_right = WindowHeap(k, False), WindowHeap(k, True)

        result: List[float] = []
        for pos in range(len(nums)):
            if pos >= k:
                heap_left.discard(nums[pos - k], pos - k)
                heap_right.discard(nums[pos - k], pos - k)

            if len(heap_right) > 0 and heap_right[0] <= nums[pos]:
                heap_right.push(nums[pos], pos)
            else:
                heap_left.push(nums[pos], pos)

            if len(heap_left) > len(heap_right):
                heap_right.push(*heap_left.pop())

            if len(heap_right) > len(heap_left):
                heap_left.push(*heap_right.pop())

            if pos >= k - 1:
                if len(heap_left) > len(heap_right):
                    result.append(float(heap_left[0]))
                else:
                    result.append((heap_left[0] + heap_right[0]) / 2.0)

        return result
