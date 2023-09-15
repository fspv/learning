import heapq
from typing import List, Tuple


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap: List[Tuple[int, int]] = [(0, 0)]

        visited = [False] * len(points)

        def distance(point1: int, point2: int) -> int:
            return abs(points[point1][0] - points[point2][0]) + abs(
                points[point1][1] - points[point2][1]
            )

        min_cost = 0
        count = 0

        while heap:
            edge_weight, point = heapq.heappop(heap)

            if visited[point]:
                continue

            visited[point] = True
            min_cost += edge_weight
            count += 1

            if count == len(points):
                break

            for adj_point in filter(
                lambda x: x != point and not visited[x], range(len(points))
            ):
                heapq.heappush(heap, (distance(point, adj_point), adj_point))

        return min_cost
