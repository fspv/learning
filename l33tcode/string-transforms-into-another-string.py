from enum import Enum
from typing import Dict, List, Set, Tuple


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        def build_adj_list(str1: str, str2: str) -> Dict[str, Set[str]]:
            adj_list: Dict[str, Set[str]] = {}

            for pos in range(len(str1)):
                adj_list.setdefault(str1[pos], set())
                adj_list.setdefault(str2[pos], set())
                adj_list[str1[pos]].add(str2[pos])

            return adj_list

        adj_list = build_adj_list(str1, str2)

        if any(len(l) > 1 for l in adj_list.values()):
            return False

        colors: Dict[str, Color] = {key: Color.WHITE for key in adj_list.keys()}

        def dfs(vertex: str) -> Tuple[bool, int]:
            if colors[vertex] == Color.BLACK:
                return True

            if colors[vertex] == Color.GRAY:
                return False

            colors[vertex] = Color.GRAY

            for adj_vertex in adj_list[vertex]:
                if adj_vertex == vertex:
                    continue

                result = dfs(adj_vertex)
                if not result:
                    return False

            colors[vertex] = Color.BLACK

            return True

        for vertex in adj_list.keys():
            result = dfs(vertex)
            if not result:
                return len(set(str2)) < 26

        return True
