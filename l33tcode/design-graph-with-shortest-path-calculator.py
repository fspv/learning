import heapq
from typing import Dict, List, Tuple


class Graph:
    _graph: Dict[int, List[Tuple[int, int]]]

    def __init__(self, n: int, edges: List[List[int]]):
        self._graph = {i: [] for i in range(n)}

        for src, dst, weight in edges:
            self.addEdge((src, dst, weight))

    def addEdge(self, edge: List[int]) -> None:
        src, dst, weight = edge

        self._graph[src].append((dst, weight))

    def shortestPath(self, node1: int, node2: int) -> int:
        heap = [(0, node1)]
        seen = {node1}

        while heap:
            distance, node = heapq.heappop(heap)
            seen.add(node)

            if node == node2:
                return distance

            for next_node, weight in self._graph[node]:
                if next_node not in seen:
                    heapq.heappush(heap, (distance + weight, next_node))

        return -1
