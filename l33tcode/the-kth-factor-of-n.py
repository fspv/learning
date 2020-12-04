import math
import heapq


class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        heap = []
        for num in range(1, int(math.sqrt(n)) + 1):
            if n % num == 0:
                div = n // num

                heapq.heappush(heap, num)

                if div != num:
                    heapq.heappush(heap, div)


        for _ in range(k - 1):
            if not heap:
                return -1
            heapq.heappop(heap)

        if not heap:
            return -1

        return heap[0]
