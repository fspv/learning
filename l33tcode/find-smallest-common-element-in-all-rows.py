import heapq

from typing import List, Tuple, Counter


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        heap: List[Tuple[int, int, int]] = []

        counter: Counter[int] = Counter()

        for row in range(len(mat)):
            heapq.heappush(heap, (mat[row][0], row, 0))
            counter[mat[row][0]] += 1

        count = len(counter)

        if count == 1:
            return mat[0][0]

        while heap:
            value, row, col = heapq.heappop(heap)

            counter[value] -= 1

            if counter[value] == 0:
                count -= 1

            if col + 1 < len(mat[row]):
                counter[mat[row][col + 1]] += 1
                if counter[mat[row][col + 1]] == 1:
                    count += 1

                heapq.heappush(heap, (mat[row][col + 1], row, col + 1))

                if count == 1:
                    return mat[row][col + 1]

        return -1
