from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output: List[int] = []

        def dfs(node: TreeNode, level: int) -> None:
            if level + 1 > len(output):
                output.append(node.val)

            if node.right:
                dfs(node.right, level + 1)

            if node.left:
                dfs(node.left, level + 1)

        if not root:
            return []

        dfs(root, 0)

        return output


class Solution1:
    def rightSideView(self, root):
        result = []

        if not root:
            return result

        stack = [root]

        while stack:
            old_stack = stack
            stack = []

            result.append(old_stack[-1].val)

            for node in old_stack:
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return result
