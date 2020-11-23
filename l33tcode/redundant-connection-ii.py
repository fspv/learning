from typing import List, DefaultDict, Set, Tuple, Dict
from enum import Enum
from collections import defaultdict


class Color(Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        def create_adj_list(edges: List[List[int]]) -> DefaultDict[int, List[int]]:
            adj_list: DefaultDict[int, List[int]] = defaultdict(list)

            for src, dst in edges:
                adj_list[src].append(dst)
                adj_list[dst]

            return adj_list

        def dfs(vertex: int) -> None:
            colors[vertex] = Color.GRAY

            for adj_vertex in adj_list[vertex]:
                if colors[adj_vertex] == Color.GRAY:
                    back_edges.add((vertex, adj_vertex))
                elif colors[adj_vertex] == Color.BLACK:
                    cross_edges.add((vertex, adj_vertex))
                else:
                    dfs(adj_vertex)

            colors[vertex] = Color.BLACK

        possible_edges: Set[Tuple[int, int]] = set()
        back_edges: Set[Tuple[int, int]] = set()
        cross_edges: Set[Tuple[int, int]] = set()
        colors: Dict[int, Color] = {}

        adj_list = create_adj_list(edges)

        for vertex in adj_list.keys():
            colors = {key: Color.WHITE for key in adj_list.keys()}
            back_edges = set()
            cross_edges = set()
            dfs(vertex)

            if all(c == Color.BLACK for c in colors.values()):
                possible_edges = possible_edges | back_edges | cross_edges

        adj_list = create_adj_list(list(reversed(edges)))

        for vertex in adj_list.keys():
            back_edges = set()
            cross_edges = set()
            colors = {key: Color.WHITE for key in adj_list.keys()}
            dfs(vertex)

            if all(c == Color.BLACK for c in colors.values()):
                possible_edges = possible_edges | back_edges | cross_edges

        for src, dst in reversed(edges):
            if (src, dst) in possible_edges:
                return [src, dst]

        raise RuntimeError("No edges to remove")
