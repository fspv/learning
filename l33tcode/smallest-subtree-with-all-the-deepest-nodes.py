# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        subtree = None
        subtree_depth = 0

        def dfs(node: Optional[TreeNode], depth: int) -> int:
            nonlocal subtree
            nonlocal subtree_depth

            if not node:
                return depth

            depth_left = dfs(node.left, depth + 1)
            depth_right = dfs(node.right, depth + 1)

            if depth_left == depth_right:
                if depth_left >= subtree_depth:
                    subtree = node
                    subtree_depth = depth_left

            return max(depth_left, depth_right)

        dfs(root, 0)

        return subtree
