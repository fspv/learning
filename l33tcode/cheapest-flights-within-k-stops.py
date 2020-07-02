import heapq
from functools import lru_cache
from typing import List
from collections import defaultdict


class Vertex:
    def __init__(self, val):
        self.val = val
        self.edges = []
        self.edge_weights = []

    def __hash__(self):
        return self.val


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        vertices = defaultdict(list)

        for src_city, dst_city, weight in flights:
            vertices[src_city].append((dst_city, weight))

        heap = [(0, 0, src)]

        while heap:
            distance, stops, vertex = heapq.heappop(heap)

            if vertex == dst:
                return distance

            for adj_vertex, weight in vertices[vertex]:
                if stops <= K:
                    heapq.heappush(
                        heap, (distance + weight, stops + 1, adj_vertex)
                    )

        return -1

    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, K: int
    ) -> int:
        # This is a working solution but takes O(n^3) time, so not accepted
        @lru_cache
        def dfs(vertex, target, edges_left):
            if edges_left < 0:
                return float("+inf")

            if vertex.val == target:
                return 0

            path_weight = float("+inf")

            for neighbour, weight in zip(vertex.edges, vertex.edge_weights):
                path_weight = min(
                    path_weight, dfs(neighbour, target, edges_left - 1) + weight
                )

            return path_weight

        vertices = {}

        for src_city, dst_city, weight in flights:
            src_vertex = vertices.setdefault(src_city, Vertex(src_city))
            dst_vertex = vertices.setdefault(dst_city, Vertex(dst_city))

            src_vertex.edges.append(dst_vertex)
            src_vertex.edge_weights.append(weight)

        weight = dfs(vertices[src], dst, K + 1)

        return weight if weight != float("+inf") else -1
