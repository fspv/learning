from typing import List, Counter
from collections import deque


class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # For large K we'll always end up with the largest number at the
        # beginning of the array
        if k > len(arr):
            return max(arr)

        # Otherwise do a simple simulation
        queue = deque(arr)

        wins: Counter[int] = Counter()

        while True:
            first, second = queue.popleft(), queue.popleft()

            if first < second:
                wins[second] += 1
                queue.appendleft(second)
                queue.append(first)
            else:
                wins[first] += 1
                queue.appendleft(first)
                queue.append(second)

            if wins[first] == k:
                return first

            if wins[second] == k:
                return second
