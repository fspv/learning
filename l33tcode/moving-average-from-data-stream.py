from collections import deque

class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self._size = size
        self._window = deque()
        self._moving_average = 0

    def next(self, val: int) -> float:
        left = self._window.popleft() if len(self._window) == self._size else self._moving_average
        self._window.append(val)
        self._moving_average += (val - left) / len(self._window)

        return self._moving_average


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
