from collections import deque


class RecentCounter:

    def __init__(self):
        self._size = 3000
        self._buckets = deque()
        self._count = 0

    def ping(self, t: int) -> int:
        while self._buckets and self._buckets[0] < t - self._size:
            self._buckets.popleft()
            self._count -= 1

        self._buckets.append(t)
        self._count += 1

        return self._count

class RecentCounter2:

    def __init__(self):
        self._size = 3000 + 1
        self._buckets = [0] * self._size
        self._count = 0
        self._prev_ts = 0

    def ping(self, t: int) -> int:
        for ts in range(max(self._prev_ts + 1, t - self._size), t + 1):
            self._count -= self._buckets[ts % self._size]
            self._buckets[ts % self._size] = 0

        self._buckets[t % self._size] = 1
        self._count += 1

        self._prev_ts = t

        return self._count


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
