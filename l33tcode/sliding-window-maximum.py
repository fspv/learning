import heapq
from typing import List, Set, Tuple, Deque
from collections import deque


class Heap:
    def __init__(self) -> None:
        self.heap: List[Tuple[int, int]] = []
        self.present: Set[Tuple[int, int]] = set()

    def push(self, value: Tuple[int, int]) -> None:
        heapq.heappush(self.heap, value)
        self.present.add(value)

    def pop(self) -> Tuple[int, int]:
        self.peek()

        return heapq.heappop(self.heap)

    def peek(self) -> Tuple[int, int]:
        while self.heap[0] not in self.present:
            heapq.heappop(self.heap)

        return self.heap[0]

    def discard(self, value: Tuple[int, int]) -> None:
        self.present.discard(value)


class Solution:
    def maxSlidingWindowHeap(self, nums: List[int], k: int) -> List[int]:
        result: List[int] = []
        heap = Heap()

        for pos in range(k):
            heap.push((-nums[pos], pos))

        if heap:
            result.append(-heap.peek()[0])

        for pos in range(k, len(nums)):
            heap.discard((-nums[pos - k], pos - k))
            heap.push((-nums[pos], pos))

            result.append(-heap.peek()[0])

        return result

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue: Deque[int] = deque()

        def add(pos: int) -> None:
            while queue and nums[queue[-1]] <= nums[pos]:
                queue.pop()

            queue.append(pos)

        def discard_left(pos: int) -> None:
            if queue[0] == pos:
                queue.popleft()

        result = []

        for pos in range(k):
            add(pos)

        result.append(nums[queue[0]])

        for pos in range(k, len(nums)):
            discard_left(pos - k)
            add(pos)
            result.append(nums[queue[0]])

        return result
