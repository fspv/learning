from typing import List, Dict
from functools import lru_cache


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_adj_list(n: int, edges: List[List[int]]) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(n)]

            for src, dst in edges:
                adj_list[src].append(dst)
                adj_list[dst].append(src)

            return adj_list

        adj_list: List[List[int]] = build_adj_list(n, edges)

        @lru_cache(None)
        def dfs(src: int, dst: int) -> int:
            max_depth = 0

            for adj_vertex in adj_list[dst]:
                if adj_vertex != src:
                    max_depth = max(max_depth, dfs(dst, adj_vertex) + 1)

            return max_depth

        heights = [0] * n

        for vertex in range(n):
            heights[vertex] = dfs(-1, vertex)

        min_height = min(heights)

        return list(filter(lambda h: heights[h] == min_height, range(len(heights))))
