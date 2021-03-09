# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: TreeNode, value: int, add_depth: int) -> TreeNode:
        def dfs(node: TreeNode, depth: int) -> None:
            node_left, node_right = node.left, node.right

            if depth == add_depth - 1:
                node.left = TreeNode(value)
                node.left.left = node_left
                node.right = TreeNode(value)
                node.right.right = node_right

            if node.left:
                dfs(node.left, depth + 1)

            if node.right:
                dfs(node.right, depth + 1)

        tmp_root = TreeNode(0)
        tmp_root.left = root

        dfs(tmp_root, 0)

        return tmp_root.left
