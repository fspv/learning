from collections import deque
from typing import Deque, List, Tuple


class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        subtree_size: List[int] = [0] * n
        depths: List[int] = [0] * n

        def build_adj_list() -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(n)]

            for src, dst in edges:
                adj_list[src].append(dst)
                adj_list[dst].append(src)

            return adj_list

        adj_list = build_adj_list()

        def dfs(node: int, parent: int, depth: int) -> int:
            depths[node] = depth

            nodes = 1

            for next_node in adj_list[node]:
                if next_node != parent:
                    nodes += dfs(next_node, node, depth + 1)

            subtree_size[node] = nodes

            return nodes

        dfs(0, 0, 0)

        distance_sum = sum(depths)
        total = subtree_size[0]

        result = [0] * n

        def dfs2(node: int, parent: int) -> None:
            nonlocal distance_sum
            nonlocal result

            result[node] = distance_sum

            for next_node in adj_list[node]:
                if next_node != parent:
                    above = total - subtree_size[next_node]
                    distance_sum += above
                    distance_sum -= subtree_size[next_node]
                    dfs2(next_node, node)
                    distance_sum -= above
                    distance_sum += subtree_size[next_node]

        dfs2(0, 0)

        return result

    def sumOfDistancesInTreeBFS(self, n: int, edges: List[List[int]]) -> List[int]:
        def build_adj_list() -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(n)]

            for src, dst in edges:
                adj_list[src].append(dst)
                adj_list[dst].append(src)

            return adj_list

        adj_list = build_adj_list()

        def bfs(vertex: int) -> int:
            count = 0

            visited: List[bool] = [False] * n
            queue: Deque[Tuple[int, int]] = deque()

            queue.append((vertex, 0))
            visited[vertex] = True

            while queue:
                this_vertex, distance = queue.popleft()
                count += distance

                for next_vertex in adj_list[this_vertex]:
                    if not visited[next_vertex]:
                        queue.append((next_vertex, distance + 1))
                        visited[next_vertex] = True

            return count

        counts: List[int] = [0] * n
        for vertex in range(n):
            counts[vertex] = bfs(vertex)

        return counts

    def sumOfDistancesInTreeFloydWarshall(
        self, n: int, edges: List[List[int]]
    ) -> List[int]:
        # N^3, TLE
        distance = [[float("+inf")] * n for _ in range(n)]

        for src, dst in edges:
            distance[src][dst] = 1
            distance[dst][src] = 1

        for vertex in range(n):
            distance[vertex][vertex] = 0

        for middle in range(n):
            for left in range(n):
                for right in range(n):
                    distance[left][right] = min(
                        distance[left][right],
                        distance[left][middle] + distance[middle][right],
                    )

        return list(map(sum, distance))
