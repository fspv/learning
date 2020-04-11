# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        def dfs(node, count):
            count_left, count_right = count, count
            radius_left, radius_right = 0, 0

            if node.left:
                count_left, radius_left = dfs(node.left, count + 1)
            if node.right:
                count_right, radius_right = dfs(node.right, count + 1)

            return (
                max(count_left, count_right),
                max(radius_left, radius_right, count_left + count_right - 2 * count),
            )

        return dfs(root, 0)[1] if root else 0
