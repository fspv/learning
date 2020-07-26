from collections import defaultdict
from typing import List, Dict, Set, Optional


class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def make_graph(dislikes: List[List[int]]) -> Dict[int, List[int]]:
            graph = defaultdict(list)
            for left, right in dislikes:
                graph[right].append(left)
                graph[left].append(right)

            return graph

        graph = make_graph(dislikes)
        colors: List[Optional[bool]] = [None] * (N + 1)

        def dfs(pos: int, color: bool) -> bool:
            if colors[pos] is not None:
                return colors[pos] == color

            colors[pos] = color

            result = True
            for neigh_pos in graph[pos]:
                result = result and dfs(neigh_pos, not color)

            return result

        result = True

        for pos in range(1, N + 1):
            if colors[pos] is None:
                result = result and dfs(pos, True)

        return result
