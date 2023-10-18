from collections import deque
from typing import Deque, Dict, List


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build graph
        graph: Dict[int, List[int]] = {src: [] for src in range(n)}
        inbound_edges = [0] * n
        for src, dst in relations:
            graph[src - 1].append(dst - 1)
            inbound_edges[dst - 1] += 1

        # Cache with the minimum time to complete all the dependencies
        not_earlier_than = [0] * n

        # Topological sort
        queue: Deque[int] = deque([v for v in range(n) if inbound_edges[v] == 0])

        while queue:
            vertex = queue.popleft()

            for next_vertex in graph[vertex]:
                inbound_edges[next_vertex] -= 1

                # Update cache
                not_earlier_than[next_vertex] = max(
                    not_earlier_than[next_vertex],
                    not_earlier_than[vertex] + time[vertex],
                )

                if inbound_edges[next_vertex] == 0:
                    queue.append(next_vertex)

        return max([not_earlier_than[v] + time[v] for v in range(n)])
