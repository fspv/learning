import heapq
from typing import List, Tuple


class Solution:
    def worker_bike_distance(self, worker: List[int], bike: List[int]) -> int:
        return abs(worker[0] - bike[0]) + abs(worker[1] - bike[1])

    def assignBikes(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        distance_buckets = [[] for _ in range(2000)]


        for worker in range(len(workers)):
            for bike in range(len(bikes)):
                distance = self.worker_bike_distance(workers[worker], bikes[bike])
                distance_buckets[distance].append((worker, bike))

        worker_bike = [-1] * len(workers)
        bike_worker = [-1] * len(bikes)
        for bucket in distance_buckets:
            for worker, bike in bucket:
                if worker_bike[worker] == -1 and bike_worker[bike] == -1:
                    worker_bike[worker] = bike
                    bike_worker[bike] = worker

        return worker_bike

    def assignBikesHeap(
        self, workers: List[List[int]], bikes: List[List[int]]
    ) -> List[int]:
        # Not accepted
        heap: List[Tuple[int, int, int]] = []

        for worker in range(len(workers)):
            for bike in range(len(bikes)):
                distance = self.worker_bike_distance(workers[worker], bikes[bike])
                heapq.heappush(heap, (distance, worker, bike))

        worker_bike = [-1] * len(workers)
        bike_worker = [-1] * len(bikes)
        while heap:
            _, worker, bike = heapq.heappop(heap)

            if worker_bike[worker] == -1 and bike_worker[bike] == -1:
                worker_bike[worker] = bike
                bike_worker[bike] = worker

        return worker_bike
