from itertools import permutations
from typing import List, Set


class UnionFind:
    def __init__(self, size: int) -> None:
        self.counts: List[int] = [1] * size
        self.roots: List[int] = list(range(size))
        self.forest_size = size

    def union(self, root_left: int, root_right: int) -> None:
        root_less, root_more = list(
            sorted([root_left, root_right], key=lambda r: -self.counts[r])
        )

        self.counts[root_more] += self.counts[root_left]
        self.roots[root_less] = root_more

        self.forest_size -= 1

    def find(self, node: int) -> int:
        if self.roots[node] == node:
            return node

        self.roots[node] = self.find(self.roots[node])

        return self.roots[node]


def mst_cost(union_find: UnionFind, edges: List[List[int]], skip_edge: int) -> int:
    cost = 0
    max_cost = 1

    for edge in range(len(edges)):
        src, dst, weight = edges[edge]
        max_cost += weight

        if edge == skip_edge:
            continue

        root_src, root_dst = union_find.find(src), union_find.find(dst)

        if root_src != root_dst:
            cost += weight
            union_find.union(root_src, root_dst)

    if union_find.forest_size > 1:
        return max_cost

    return cost


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self, n: int, edges: List[List[int]]
    ) -> List[List[int]]:
        pos_map: List[int] = []
        edges_sorted: List[List[int]] = []

        for pos, edge in sorted(enumerate(edges), key=lambda x: x[1][2]):
            pos_map.append(pos)
            edges_sorted.append(edge)

        edges = edges_sorted

        union_find = UnionFind(n)
        min_cost = mst_cost(union_find, edges, -1)
        critical: List[int] = []
        pseudo_critical: List[int] = []

        for skip_edge in range(len(edges)):
            union_find = UnionFind(n)
            cost = mst_cost(union_find, edges, skip_edge)
            if cost != min_cost:
                critical.append(pos_map[skip_edge])
            elif cost == min_cost:
                union_find = UnionFind(n)
                union_find.union(edges[skip_edge][0], edges[skip_edge][1])
                cost_with = edges[skip_edge][2] + mst_cost(union_find, edges, skip_edge)
                if cost_with == cost:
                    pseudo_critical.append(pos_map[skip_edge])

        return [critical, pseudo_critical]
