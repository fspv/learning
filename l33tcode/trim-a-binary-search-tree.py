from typing import Optional, List, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        if not root:
            return None

        new_root = TreeNode(root.val)
        new_root.right = root

        stack: List[Tuple[Optional[TreeNode], Optional[TreeNode], TreeNode]] = [
            (new_root, new_root, root)
        ]

        while stack:
            parent_left, parent_right, node = stack.pop()

            if low <= node.val <= high:
                if parent_left:
                    parent_left.left = node
                if parent_right:
                    parent_right.right = node

            if node.left:
                if low <= node.val <= high:
                    stack.append((node, None, node.left))
                    node.left = None
                else:
                    stack.append((parent_left, parent_right, node.left))

            if node.right:
                if low <= node.val <= high:
                    stack.append((None, node, node.right))
                    node.right = None
                else:
                    stack.append((parent_left, parent_right, node.right))

        return new_root.left or new_root.right

    def trimBSTRecursive(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def dfs(node: TreeNode) -> TreeNode:
            if node.left:
                node.left = dfs(node.left)

            if node.right:
                node.right = dfs(node.right)

            if low <= node.val <= high:
                return node
            elif node.val < low:
                return node.right
            else:
                return node.left

        if not root:
            return None

        return dfs(root)

    def trimBSTFirst(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        def dfs(node):
            if node.left:
                node.left = dfs(node.left)
            if node.right:
                node.right = dfs(node.right)

            if node.val < L:
                return node.right
            elif node.val > R:
                return node.left
            else:
                return node

        return dfs(root)
