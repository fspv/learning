import heapq
from typing import List, Tuple
from collections import deque
from functools import lru_cache
from itertools import combinations


class Solution:
    def minNumberOfSemesters(
        self, n: int, dependencies: List[List[int]], k: int
    ) -> int:
        def init_adj_list(n: int, dependencies: List[List[int]]) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(n)]

            for vertex, adj_vertex in dependencies:
                adj_list[vertex - 1].append(adj_vertex - 1)

            return adj_list

        adj_list = init_adj_list(n, dependencies)
        indegree = [0] * n

        for vertex in range(n):
            for adj_vertex in adj_list[vertex]:
                indegree[adj_vertex] += 1

        @lru_cache(None)
        def dfs(bitmap: int) -> int:
            available_vertices: List[int] = []

            min_semesters = n

            for vertex, vertex_indegree in enumerate(indegree):
                if bitmap & (1 << vertex) == 0 and vertex_indegree == 0:
                    available_vertices.append(vertex)

            if not available_vertices:
                return 0

            for vertices in combinations(available_vertices, min(k, len(available_vertices))):
                for vertex in vertices:
                    bitmap |= 1 << vertex
                    for adj_vertex in adj_list[vertex]:
                        indegree[adj_vertex] -= 1

                min_semesters = min(min_semesters, dfs(bitmap) + 1)

                for vertex in vertices:
                    bitmap ^= 1 << vertex
                    for adj_vertex in adj_list[vertex]:
                        indegree[adj_vertex] += 1

            return min_semesters

        return dfs(0)
