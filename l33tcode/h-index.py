import heapq


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        heap = []

        for number in citations:
            heapq.heappush(heap, number)
            if heap[0] < len(heap):
                heapq.heappop(heap)

        return len(heap)
