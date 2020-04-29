# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> (int, int):
            max_sum, max_path = node.val, node.val

            if node.left:
                max_sum_left, max_path_left = dfs(node.left)
                max_path = max(max_path, max_path_left + node.val)
                max_sum = max(max_sum, max_sum_left, max_path)

            if node.right:
                max_sum_right, max_path_right = dfs(node.right)
                max_path = max(max_path, max_path_right + node.val)
                max_sum = max(max_sum, max_sum_right, max_path)

            if node.left and node.right:
                max_sum = max(max_sum, max_path_left + max_path_right + node.val)

            return max_sum, max_path

        return dfs(root)[0]
