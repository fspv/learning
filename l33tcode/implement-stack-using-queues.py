from collections import deque
from typing import Deque


class MyStack:
    _queue: Deque[int]

    def __init__(self):
        self._queue: Deque[int] = deque()

    def push(self, x: int) -> None:
        self._queue.append(x)

    def pop(self) -> int:
        self._queue.rotate(-(len(self._queue) - 1))

        return self._queue.popleft()

    def top(self) -> int:
        result = self.pop()
        self.push(result)

        return result

    def empty(self) -> bool:
        return len(self._queue) == 0
