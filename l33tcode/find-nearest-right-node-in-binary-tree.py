from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findNearestRightNode(
        self, root: TreeNode, target: TreeNode
    ) -> Optional[TreeNode]:
        target_row = 0
        next_in_row: Optional[TreeNode] = None

        def find_next_in_row(node: TreeNode, row: int) -> None:
            nonlocal next_in_row

            if target_row == row:
                next_in_row = next_in_row or node
                return

            if node.left:
                find_next_in_row(node.left, row + 1)

            if node.right:
                find_next_in_row(node.right, row + 1)

        def find_node(node: TreeNode, row: int) -> bool:
            nonlocal target_row

            if node == target:
                target_row = row
                return True

            found = False

            if node.left:
                found = found or find_node(node.left, row + 1)

            if node.right:
                if found:
                    find_next_in_row(node.right, row + 1)
                else:
                    found = found or find_node(node.right, row + 1)

            return found

        if not root:
            return None

        find_node(root, 0)

        return next_in_row
