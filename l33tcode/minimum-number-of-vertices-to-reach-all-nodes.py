from typing import List, Set


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_adj_list(n: int, edges: List[List[int]]) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(n)]

            for start, end in edges:
                adj_list[start].append(end)

            return adj_list

        result: Set[int] = set()

        def dfs(node: int, adj_list: List[List[int]], visited: Set[int]) -> None:
            if node in result:
                result.remove(node)

            if node in visited:
                return

            visited.add(node)

            for next_node in adj_list[node]:
                dfs(next_node, adj_list, visited)

        visited: Set[int] = set()
        adj_list = build_adj_list(n, edges)

        for vertex in range(n):
            if vertex not in visited:
                dfs(vertex, adj_list, visited)
                result.add(vertex)

        return list(result)
