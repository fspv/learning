from enum import Enum
from typing import List


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def build_adj_list(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj_list: List[List[int]] = [[] for _ in range(n)]

        for src, dst in edges:
            adj_list[src].append(dst)

        return adj_list

    def leadsToDestination(
        self, n: int, edges: List[List[int]], source: int, destination: int
    ) -> bool:
        adj_list = self.build_adj_list(n, edges)
        colors = [Color.WHITE] * n

        def dfs(node: int) -> bool:
            if colors[node] == Color.GRAY:
                return False

            if colors[node] == Color.BLACK:
                return True

            colors[node] = Color.GRAY

            result = True

            if not adj_list[node]:
                result = node == destination

            for next_node in adj_list[node]:
                result = result and dfs(next_node)

            colors[node] = Color.BLACK

            return result

        return dfs(source)
