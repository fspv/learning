# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, max_so_far: int) -> int:
            count = 0
            if node.val >= max_so_far:
                count += 1

            max_so_far = max(node.val, max_so_far)

            if node.left:
                count += dfs(node.left, max_so_far)

            if node.right:
                count += dfs(node.right, max_so_far)

            return count

        return dfs(root, float("-inf"))
