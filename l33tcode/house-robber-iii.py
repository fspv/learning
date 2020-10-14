from functools import lru_cache


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(None)
        def dfs(node: TreeNode, can_take: bool) -> int:
            if not node:
                return 0

            return max(
                node.val + dfs(node.left, False) + dfs(node.right, False)
                if can_take
                else 0,
                dfs(node.left, True) + dfs(node.right, True),
            )

        return dfs(root, True)
