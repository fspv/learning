from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def find(array: List[int], pos: int):
            root = pos
            while root != array[root]:
                root = array[root]
            while pos != root:
                array[pos], pos = root, array[pos]
            return root

        def union(root_left: int, root_right: int, array: List[int], count: List[int]):
            root_less, root_more = sorted(
                (root_left, root_right), key=lambda x: count[x]
            )

            array[root_less] = root_more
            count[root_more] += count[root_less]

        array = list(range(n))
        count = [1] * n
        groups = n

        for left, right in edges:
            root_left = find(array, left)
            root_right = find(array, right)

            if root_left == root_right:
                return False
            else:
                union(root_left, root_right, array, count)
                groups -= 1

        return groups == 1
