# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        def dfs(node: TreeNode, closest: int) -> int:
            closest = min(closest, node.val, key=lambda x: abs(x - target))
            if node.left:
                closest = dfs(node.left, closest)
            if node.right:
                closest = dfs(node.right, closest)

            return closest

        return dfs(root, float("-inf"))
