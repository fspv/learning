import heapq
from typing import List, Tuple
from functools import lru_cache


class Worker:
    def __init__(self, wage: float, quality: float) -> None:
        self.wage = wage
        self.quality = quality
        self.ratio = wage / quality


class Solution:
    def mincostToHireWorkers(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        workers = [Worker(w, q) for w, q in zip(wage, quality)]
        workers.sort(key=lambda w: w.ratio)

        cost = float("+inf")
        total_quality = 0
        heap = []
        for worker in workers:
            heapq.heappush(heap, -worker.quality)
            total_quality += worker.quality

            if len(heap) > K:
                total_quality -= -heapq.heappop(heap)

            if len(heap) == K:
                cost = min(cost, total_quality * worker.ratio)

        return cost

    def mincostToHireWorkersBruteForceDFS(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        @lru_cache(None)
        def dfs(worker: int, left: int, ratio: float, prev: float) -> float:
            if left == 0:
                return prev

            if worker == len(quality):
                return float("+inf")

            cur_wage = max(quality[worker] * ratio, wage[worker])
            cur_ratio = cur_wage / quality[worker]

            total_wage = prev * cur_ratio / ratio + cur_wage

            return min(
                dfs(worker + 1, left, ratio, prev),
                dfs(worker + 1, left - 1, cur_ratio, total_wage),
            )

        return dfs(0, K, 0.000001, 0)

    def mincostToHireWorkersBruteForceDijkstra(
        self, quality: List[int], wage: List[int], K: int
    ) -> float:
        wage_quality = list(
            reversed(
                sorted(((w, q) for w, q in zip(wage, quality)), key=lambda x: (x[0] / x[1]))
            )
        )

        heap = []
        heapq.heappush(heap, (0, K, 0, 0))

        while heap:
            prev_wage, left, ratio, worker = heapq.heappop(heap)

            if left == 0:
                return prev_wage

            if worker == len(quality):
                continue

            heapq.heappush(heap, (prev_wage, left, ratio, worker + 1))

            cur_wage, cur_quality = wage_quality[worker]
            ratio = max(ratio, cur_wage / cur_quality)
            new_wage = prev_wage + cur_quality * ratio

            heapq.heappush(heap, (new_wage, left - 1, ratio, worker + 1))


        return -1.0
