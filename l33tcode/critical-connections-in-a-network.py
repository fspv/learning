from typing import List, Iterator


class Solution:
    def criticalConnections(
        self, n: int, connections: List[List[int]]
    ) -> List[List[int]]:
        adj_list: List[List[int]] = [[] for _ in range(n)]

        for src, dst in connections:
            adj_list[src].append(dst)
            adj_list[dst].append(src)

        visited = [False] * n
        times = [0] * n
        low_times = [0] * n

        result = []

        def dfs(pos: int, parent: int, time: int) -> int:
            times[pos] = time
            low_times[pos] = time

            for neigh_pos in adj_list[pos]:
                if not visited[neigh_pos]:
                    time += 1
                    visited[neigh_pos] = True
                    time = dfs(neigh_pos, pos, time)

                if neigh_pos != parent:
                    low_times[pos] = min(low_times[pos], low_times[neigh_pos])

            if times[pos] <= low_times[pos] and parent != -1:
                result.append([pos, parent])

            return time

        for pos in range(n):
            if not visited[pos]:
                visited[pos] = True
                dfs(pos, -1, 0)

        return result
