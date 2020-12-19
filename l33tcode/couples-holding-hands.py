import math
from typing import List, Set


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        reverse_index: List[Set[int]] = [set() for _ in range(len(row) // 2)]

        for seat in range(len(row)):
            reverse_index[row[seat] // 2].add(seat)

        visited = [False] * (len(row) // 2)

        min_swaps = 0

        for init_seat in range(len(row)):
            if visited[init_seat // 2]:
                continue

            visited[init_seat // 2] = True

            loop_len = 0
            seat = init_seat

            while (
                seat := (reverse_index[row[seat] // 2] - {seat}).pop()
            ) // 2 != init_seat // 2:
                visited[seat // 2] = True
                seat = (seat // 2 + 1) * 2 - 1 - seat % 2
                visited[seat // 2] = True
                loop_len += 1

            min_swaps += loop_len

        return min_swaps
