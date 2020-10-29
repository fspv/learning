from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        start = -1

        max_distance = 0

        for pos in range(len(seats)):
            if seats[pos] == 1:
                if start == -1:
                    start = -pos
                max_distance = max(max_distance, (pos - start) // 2)
                start = pos

        max_distance = max(max_distance, len(seats) - 1 - start)

        return max_distance
