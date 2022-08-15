from typing import List


class UnionFind:
    def __init__(self, size: int) -> None:
        self._roots: List[int] = list(range(size))
        self._counts: List[int] = [0] * size

    def find(self, vertex: int) -> int:
        if vertex != self._roots[vertex]:
            self._roots[vertex] = self.find(self._roots[vertex])

        return self._roots[vertex]

    def union(self, left: int, right: int) -> None:
        less, more = sorted(
            [self.find(left), self.find(right)], key=lambda x: self._counts[x]
        )

        self._roots[less] = self._roots[more]
        self._counts[more] += self._counts[less]


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(max(map(lambda x: max(x), edges)) + 1)

        for left, right in edges:
            if union_find.find(left) == union_find.find(right):
                return [left, right]
            else:
                union_find.union(left, right)

        return []
