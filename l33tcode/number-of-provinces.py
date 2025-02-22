from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        def find(array: List[int], pos: int):
            root = pos
            while root != array[root]:
                root = array[root]
            while pos != root:
                array[pos], pos = root, array[pos]
            return root

        def union(root_left: int, root_right: int, array: List[int], count: List[int]):
            root_more, root_less = sorted(
                (root_left, root_right), key=lambda x: count[x]
            )

            array[root_less] = root_more
            count[root_more] += count[root_less]

        disj_set = list(range(len(M)))
        count = [1] * len(M)
        result = len(M)

        for row in range(len(M)):
            for col in range(row + 1, len(M[0])):
                if M[row][col]:
                    root_left = find(disj_set, row)
                    root_right = find(disj_set, col)

                    if root_left != root_right:
                        union(root_left, root_right, disj_set, count)
                        result -= 1

        return result
