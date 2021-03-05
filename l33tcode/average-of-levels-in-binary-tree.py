from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        counts: List[int] = []
        avg: List[float] = []

        def dfs(node: TreeNode, depth: int) -> None:
            if len(counts) < depth + 1:
                counts.append(0)
                avg.append(0)

            counts[depth] += 1
            avg[depth] = (avg[depth] * (counts[depth] - 1) + node.val) / counts[depth]

            if node.left:
                dfs(node.left, depth + 1)

            if node.right:
                dfs(node.right, depth + 1)

        dfs(root, 0)

        return avg
