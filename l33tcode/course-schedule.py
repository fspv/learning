from typing import List, Deque
from collections import deque


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def build_adj_list(
            num_courses: int, prerequisites: List[List[int]]
        ) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(num_courses)]

            for src, dst in prerequisites:
                adj_list[src].append(dst)

            return adj_list

        def build_indegrees(adj_list: List[List[int]]) -> List[int]:
            indegrees: List[int] = [0 for _ in adj_list]

            for src in range(len(adj_list)):
                for dst in adj_list[src]:
                    indegrees[dst] += 1

            return indegrees

        def topological_sort(
            adj_list: List[List[int]], indegrees: List[int]
        ) -> List[int]:
            queue: Deque[int] = deque()

            for vertex in range(len(indegrees)):
                if indegrees[vertex] == 0:
                    queue.append(vertex)

            result: List[int] = []

            while queue:
                vertex = queue.popleft()
                result.append(vertex)

                for adj_vertex in adj_list[vertex]:
                    indegrees[adj_vertex] -= 1
                    if indegrees[adj_vertex] == 0:
                        queue.append(adj_vertex)

            return result

        adj_list = build_adj_list(numCourses, prerequisites)
        indegrees = build_indegrees(adj_list)

        result = topological_sort(adj_list, indegrees)

        return len(result) == numCourses
