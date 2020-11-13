import heapq
from typing import List, Tuple
from collections import Counter


class Solution:
    def reorganizeString(self, S: str) -> str:
        heap: List[Tuple[int, str]] = []

        for char, count in Counter(S).items():
            heapq.heappush(heap, (-count, char))

        result = []

        while heap:
            if len(heap) < 2:
                break

            left_count, left_char = heapq.heappop(heap)
            right_count, right_char = heapq.heappop(heap)
            left_count *= -1
            right_count *= -1

            while right_count > 0:
                result.append(left_char)
                result.append(right_char)
                left_count -= 1
                right_count -= 1

            heapq.heappush(heap, (-left_count, left_char))

        if heap:
            count = -heap[0][0]

            if count > 1:
                return ""
            elif count != 0:
                result.append(heap[0][1])

        return "".join(result)
