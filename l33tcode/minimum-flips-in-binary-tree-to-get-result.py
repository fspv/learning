from typing import Dict, Tuple

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minimumFlips(self, root: Optional[TreeNode], result: bool) -> int:
        def dfs(node: TreeNode) -> Tuple[int, int]:
            left, right = (0, 0), (0, 0)

            if node.left:
                left = dfs(node.left)

            if node.right:
                right = dfs(node.right)

            if node.val == 0:
                return (0, 1)
            elif node.val == 1:
                return (1, 0)
            elif node.val == 2:  # OR
                # 0 0 0
                # 0 1 1
                # 1 0 1
                # 1 1 1

                return (
                    left[0] + right[0],
                    min(left[0] + right[1], left[1] + right[0], left[1] + right[1]),
                )
            elif node.val == 3:  # AND
                # 0 0 0
                # 0 1 0
                # 1 0 0
                # 1 1 1
                return (
                    min(left[0] + right[1], left[1] + right[0], left[0] + right[0]),
                    left[1] + right[1],
                )
            elif node.val == 4:  # XOR
                # 0 0 0
                # 0 1 1
                # 1 0 1
                # 1 1 0
                return (
                    min(left[0] + right[0], left[1] + right[1]),
                    min(left[1] + right[0], left[0] + right[1]),
                )
            elif node.val == 5:  # NOT
                # 0 x 1
                # 1 x 0
                # x 0 1
                # x 1 0
                return (
                    left[1] + right[1],
                    left[0] + right[0],
                )
            else:
                raise ValueError(f"Operation {node.val} is not defined")

        if not root:
            return 0  # Actually if root.val != result we might want to return smth else

        return dfs(root)[result]
