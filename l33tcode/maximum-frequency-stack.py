import heapq
from collections import Counter, defaultdict


class FreqStack:

    def __init__(self):
        self._counts = Counter()
        self._freq_stack = defaultdict(list)
        self._max_freq = 0

    def push(self, x: int) -> None:
        self._counts[x] += 1
        self._freq_stack[self._counts[x]].append(x)
        self._max_freq = max(self._counts[x], self._max_freq)

    def pop(self) -> int:
        val = self._freq_stack[self._max_freq].pop()
        self._counts[val] -= 1

        if not self._freq_stack[self._max_freq]:
            self._max_freq -= 1

        return val


class FreqStackHeap:  # log N push and pop, suboptimal

    def __init__(self):
        self._counts = Counter()
        self._heap = []
        self._pos = 0

    def push(self, x: int) -> None:
        self._counts[x] += 1
        self._pos += 1  # should be mod maxint in the real code
        heapq.heappush(self._heap, (-self._counts[x], -(self._pos + 1), x))

    def pop(self) -> int:
        _, _, val = heapq.heappop(self._heap)
        self._counts[val] -= 1
        return val



# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
