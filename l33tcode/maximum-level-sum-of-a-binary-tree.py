# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(node, level, level_sums):
            if not node:
                return

            if len(level_sums) < level + 1:
                level_sums.append(0)

            level_sums[level] += node.val

            dfs(node.left, level + 1, level_sums)
            dfs(node.right, level + 1, level_sums)

        level_sums = []
        dfs(root, 0, level_sums)

        max_level_sum = max(level_sums)

        for pos, level_sum in enumerate(level_sums):
            if level_sum == max_level_sum:
                return pos + 1
