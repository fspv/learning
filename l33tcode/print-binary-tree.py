from typing import Tuple, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_size(root: TreeNode) -> Tuple[int, int]:
            def dfs_height(node: TreeNode) -> int:
                if not node:
                    return 0

                return max(dfs_height(node.left), dfs_height(node.right)) + 1

            rows = dfs_height(root)
            cols = 2 ** rows - 1

            return rows, cols

        def create_matrix(rows: int, cols: int) -> List[List[str]]:
            return [[""] * cols for _ in range(rows)]

        def dfs(
            node: TreeNode,
            row: int,
            left_col: int,
            right_col: int,
            matrix: List[List[str]],
        ) -> None:
            if not node:
                return

            middle_col = left_col + (right_col - left_col) // 2

            matrix[row][middle_col] = str(node.val)

            dfs(node.left, row + 1, left_col, middle_col, matrix)
            dfs(node.right, row + 1, middle_col + 1, right_col, matrix)

        rows, cols = get_size(root)
        matrix = create_matrix(rows, cols)

        dfs(root, 0, 0, cols, matrix)

        return matrix
