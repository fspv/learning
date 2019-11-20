from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def dfs(start, stop):
            subtrees = []

            for pos in range(start, stop):
                for left in dfs(start, pos) or [None]:
                    for right in dfs(pos + 1, stop) or [None]:
                        node = TreeNode(pos)
                        node.left, node.right = left, right

                        subtrees.append(node)

            return subtrees

        return dfs(1, n + 1)
