import heapq
from typing import List, Set


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> int:
        def distance(
            worker_pos: int, bike_pos: int
        ) -> int:
            worker_row, worker_col = workers[worker_pos]
            bike_row, bike_col = bikes[bike_pos]

            return abs(worker_row - bike_row) + abs(worker_col - bike_col)

        heap = [[0, 0, 0]]

        seen = set()

        while heap:
            dist, worker_pos, bikes_bitmap = heapq.heappop(heap)

            if worker_pos == len(workers):
                return dist

            if (worker_pos, bikes_bitmap) in seen:
                continue

            seen.add((worker_pos, bikes_bitmap))

            for bike_pos in range(len(bikes)):
                if (1 << bike_pos) & bikes_bitmap:
                    continue

                new_bikes = bikes_bitmap | (1 << bike_pos)
                heapq.heappush(
                    heap,
                    [
                        dist + distance(worker_pos, bike_pos),
                        worker_pos + 1,
                        new_bikes,
                    ],
                )

        return 0
