from typing import List


class UnionFind:
    def __init__(self, vertices: int) -> None:
        self._tree = list(range(vertices))
        self._count = [0] * vertices

    def find(self, vertex: int) -> int:
        start = vertex
        root = vertex

        while root != self._tree[root]:
            root = self._tree[root]

        while start != root:
            start, self._tree[start] = self._tree[start], root

        return root

    def union(self, root_left: int, root_right: int) -> None:
        root_less, root_more = list(
            sorted([root_left, root_right], key=lambda x: self._count[x])
        )

        self._tree[root_less] = root_more
        self._count[root_more] += self._count[root_less]


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = n

        union_find = UnionFind(n)

        for src, dst in edges:
            root_left, root_right = union_find.find(src), union_find.find(dst)

            if root_left != root_right:
                count -= 1
                union_find.union(root_left, root_right)

        return count
