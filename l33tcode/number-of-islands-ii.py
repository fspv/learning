from typing import List, Optional


class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        def find(array: List[int], pos: int) -> int:
            root = pos

            while root != array[root]:
                root = array[root]

            while pos != root:
                array[pos], pos = root, array[pos]

            return root

        def union(
            root_left: int,
            root_right: int,
            array: List[int],
            count: List[int],
        ) -> None:
            root_less, root_more = sorted(
                (root_left, root_right), key=lambda x: count[x]
            )

            array[root_less] = root_more
            count[root_more] += count[root_less]

        FAKE_ROOT = -1
        array = [FAKE_ROOT] * m * n
        count = [1] * m * n
        num_of_islands = 0
        arr_pos = lambda r, c: r * n + c
        result = []

        for row, col in positions:
            if array[arr_pos(row, col)] == FAKE_ROOT:
                array[arr_pos(row, col)] = arr_pos(row, col)
                num_of_islands += 1

                for row_next, col_next in (
                    (row - 1, col),
                    (row + 1, col),
                    (row, col - 1),
                    (row, col + 1),
                ):
                    if (
                        0 <= row_next < m
                        and 0 <= col_next < n
                        and array[arr_pos(row_next, col_next)] != FAKE_ROOT
                    ):
                        root_left = find(array, arr_pos(row, col))
                        root_right = find(array, arr_pos(row_next, col_next))

                        if root_left != root_right:
                            union(root_left, root_right, array, count)
                            num_of_islands -= 1

            result.append(num_of_islands)

        return result
