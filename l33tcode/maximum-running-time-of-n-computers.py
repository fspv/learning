import heapq
from typing import List

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        heap = [-battery for battery in batteries]
        heapq.heapify(heap)

        running_time = 0

        while len(heap) >= n:
            running_on = []

            for _ in range(n):
                running_on.append(-heapq.heappop(heap))

            for battery in running_on:
                if battery > 1:
                    heapq.heappush(heap, -(battery - 1))

            running_time += 1

        return running_time
