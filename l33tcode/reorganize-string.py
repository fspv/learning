import heapq
from typing import Counter, List, Tuple

class Solution:
    def reorganizeString(self, s: str) -> str:
        heap: List[Tuple[int, str]] = [(-count, char) for char, count in Counter(s).items()]
        heapq.heapify(heap)

        result: List[str] = []
        last_char = ""

        while len(heap) > 1:
            first, second = heapq.heappop(heap), heapq.heappop(heap)

            first_count, first_char = -first[0], first[1]
            second_count, second_char = -second[0], second[1]

            if first_char != last_char:
                result.append(first_char)
                last_char = first_char
                first_count -= 1

            if second_char != last_char:
                result.append(second_char)
                last_char = second_char
                second_count -= 1

            if first_count > 0:
                heapq.heappush(heap, (-first_count, first_char))

            if second_count > 0:
                heapq.heappush(heap, (-second_count, second_char))

        if heap:
            # Take care of the last remaining character
            if -heap[0][0] == 1 and heap[0][1] != last_char:
                result.append(heap[0][1])
            else:
                return ""

        return "".join(result)
