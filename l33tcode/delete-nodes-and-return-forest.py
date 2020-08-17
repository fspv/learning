from typing import Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        new_roots = []
        to_delete_set = set(to_delete)

        def dfs(node: Optional[TreeNode]) -> bool:
            if not node:
                return

            if node.val in to_delete_set:
                if node.left:
                    new_roots.append(node.left)
                if node.right:
                    new_roots.append(node.right)

            if dfs(node.left):
                node.left = None

            if dfs(node.right):
                node.right = None

            return node.val in to_delete_set

        if not dfs(root):
            new_roots.append(root)

        result = []

        for root in new_roots:
            if root.val not in to_delete_set:
                result.append(root)

        return result
