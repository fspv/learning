from enum import Enum
from typing import List


class Color(Enum):
    RED = 0
    BLUE = 1
    UNCOLORED = 2


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colors: List[Color] = [Color.UNCOLORED] * len(graph)

        for start_vertex in range(len(graph)):
            if colors[start_vertex] != Color.UNCOLORED:
                continue

            colors[start_vertex] = Color.RED

            stack: List[int] = [start_vertex]

            while stack:
                vertex = stack.pop()
                vertex_next_color = Color.BLUE if colors[vertex] == Color.RED else Color.RED

                for adj_vertex in graph[vertex]:
                    if colors[adj_vertex] == Color.UNCOLORED:
                        colors[adj_vertex] = vertex_next_color
                        stack.append(adj_vertex)
                    elif colors[adj_vertex] != vertex_next_color:
                        return False

        return True
