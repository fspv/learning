import heapq

from typing import List


class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        heap1 = list(map(lambda x: (-x[1], x[0]), list(enumerate(A))))
        heap2 = list(map(lambda x: (-x[1], x[0]), list(enumerate(B))))
        heapq.heapify(heap1)
        heapq.heapify(heap2)

        skipped: List[int] = []
        result = [0] * len(heap2)

        while heap2:
            heap1_val, heap1_pos = heap1[0]
            heap2_val, heap2_pos = heap2[0]

            if heap2_val <= heap1_val:
                heapq.heappop(heap2)
                skipped.append(heap2_pos)
            else:
                heapq.heappop(heap1)
                heapq.heappop(heap2)
                result[heap2_pos] = -heap1_val

        for pos in skipped:
            value, _ = heapq.heappop(heap1)
            result[pos] = -value

        return result
