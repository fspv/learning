from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, direction: Optional[bool], count: int, max_count: int):
            # direction: True - left, False - right, None - root node
            max_count = max(max_count, count)

            if node.left:
                max_count = max(
                    max_count,
                    dfs(
                        node.left,
                        True,
                        1 if direction == True else count + 1,
                        max_count,
                    ),
                )
            if node.right:
                max_count = max(
                    max_count,
                    dfs(
                        node.right,
                        False,
                        1 if direction == False else count + 1,
                        max_count,
                    ),
                )

            return max_count

        return dfs(root, None, 0, 0)
