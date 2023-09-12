import heapq
from typing import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counts = Counter(Counter(s).values())
        heap = [-num for num in counts.keys()]
        heapq.heapify(heap)

        deletions = 0

        while heap:
            num = -heapq.heappop(heap)
            count = counts[num]

            if count > 1:
                deletions += count - 1
                counts[num] -= count - 1
                if num - 1 > 0:
                    counts[num - 1] += count - 1
                    heapq.heappush(heap, -num + 1)

        return deletions
