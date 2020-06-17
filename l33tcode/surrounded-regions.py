from typing import List, Tuple, Iterator


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        surrounded = {}
        # These 2 can be flattened to array, which will give x2 space efficiency
        union_find = [
            [(row, col) for col in range(len(board[row]))] for row in range(len(board))
        ]
        counts = [[1 for col in range(len(board[row]))] for row in range(len(board))]

        def find(
            row: int, col: int, union_find: List[List[Tuple[int, int]]]
        ) -> Tuple[int, int]:
            root_row, root_col = row, col

            while union_find[root_row][root_col] != (root_row, root_col):
                root_row, root_col = union_find[root_row][root_col]

            while (row, col) != (root_row, root_col):
                tmp = union_find[row][col]
                union_find[row][col] = (root_row, root_col)
                row, col = tmp

            return (root_row, root_col)

        def union(
            root_left_row: int,
            root_left_col: int,
            root_right_row: int,
            root_right_col: int,
            counts: List[List[int]],
            union_find: List[List[Tuple[int, int]]],
        ) -> Tuple[int, int]:  # returns new root
            root_less_row, root_less_col, root_more_row, root_more_col = (
                root_left_row,
                root_left_col,
                root_right_row,
                root_right_col,
            )
            if (
                counts[root_left_row][root_left_col]
                > counts[root_right_row][root_right_col]
            ):
                root_more_row, root_more_col, root_less_row, root_less_col = (
                    root_left_row,
                    root_left_col,
                    root_right_row,
                    root_right_col,
                )

            counts[root_more_row][root_more_col] += counts[root_less_row][root_less_col]
            union_find[root_less_row][root_less_col] = union_find[root_more_row][
                root_more_col
            ]

            return root_more_row, root_more_col

        def neighbours(
            row: int, col: int, board: List[List[str]]
        ) -> Iterator[Tuple[int, int]]:
            # We can to take into accoutn only neighbours that are above or
            # to the left because those to the right and below will be attached
            # to the disjoint set during the next iterations
            for new_row, new_col in [
                (row - 1, col),
                (row, col - 1),
            ]:
                if (
                    0 <= new_row < len(board)
                    and 0 <= new_col < len(board[row])
                    and board[new_row][new_col] == "O"
                ):
                    yield new_row, new_col

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != "O":
                    continue

                surrounded[find(row, col, union_find)] = row not in (
                    0,
                    len(board) - 1,
                ) and col not in (0, len(board[0]) - 1)

                for neigh_row, neigh_col in neighbours(row, col, board):
                    root_this_row, root_this_col = find(row, col, union_find)
                    root_neigh_row, root_neigh_col = find(
                        neigh_row, neigh_col, union_find
                    )

                    if (root_this_row, root_this_col) == (
                        root_neigh_row,
                        root_neigh_col,
                    ):
                        continue

                    root_new_row, root_new_col = union(
                        root_this_row,
                        root_this_col,
                        root_neigh_row,
                        root_neigh_col,
                        counts,
                        union_find,
                    )

                    surrounded[(root_new_row, root_new_col)] = (
                        surrounded[(root_this_row, root_this_col)]
                        and surrounded[(root_neigh_row, root_neigh_col)]
                    )

        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "O" and surrounded[find(row, col, union_find)]:
                    board[row][col] = "X"
