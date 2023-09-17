from collections import deque
from typing import Deque, List, Set, Tuple


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        # (path_len, vertice, bitmask)
        queue: Deque[Tuple[int, int, int]] = deque()

        # We can visit same vertice twice, but no sense in visiting it with the
        # same set of nodes we visited before
        seen: Set[Tuple[int, int]] = set()

        # Start bruteforce from all the vertices at once
        for vertice in range(len(graph)):
            queue.append((0, vertice, 1 << vertice))
            seen.add((vertice, 1 << vertice))

        # BFS
        while queue:
            path_len, vertice, bitmask = queue.popleft()

            for next_vertice in graph[vertice]:
                next_bitmask = bitmask | (1 << next_vertice)

                if next_bitmask == (1 << len(graph)) - 1:
                    return path_len + 1

                if (next_vertice, next_bitmask) in seen:
                    continue

                seen.add((next_vertice, next_bitmask))
                queue.append((path_len + 1, next_vertice, next_bitmask))

        # BFS executed 0 times => just one node
        return 0
