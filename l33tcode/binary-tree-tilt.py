# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> Tuple[int, int]:
            left_nodes_sum, left_tilts_sum = 0, 0
            if node.left:
                left_nodes_sum, left_tilts_sum = dfs(node.left)

            right_nodes_sum, right_tilts_sum = 0, 0
            if node.right:
                right_nodes_sum, right_tilts_sum = dfs(node.right)

            return (
                left_nodes_sum + right_nodes_sum + node.val,
                abs(left_nodes_sum - right_nodes_sum)
                + left_tilts_sum
                + right_tilts_sum,
            )

        if not root:
            return 0

        return dfs(root)[1]
