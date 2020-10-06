from typing import Tuple 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def find(root: TreeNode, key: int) -> Tuple[TreeNode, TreeNode]:
            node = root
            parent = None

            while node:
                if node.val < key:
                    parent = node
                    node = node.right
                elif node.val > key:
                    parent = node
                    node = node.left
                else:
                    return parent, node

            return parent, None

        def assign_node(parent: TreeNode, node: Optional[TreeNode], val: int) -> None:
            if parent.val < val:
                parent.right = node
            elif parent.val > val:
                parent.left = node
            else:
                raise RuntimeError("Expect unique values in the tree")

        def insert(root: TreeNode, node: TreeNode) -> None:
            parent, _ = find(root, node.val)
            assign_node(parent, node, node.val)

        parent, node = find(root, key)

        if not node:
            return root

        if node.left and node.right:
            insert(node.left, node.right)

        if parent:
            if node.left:
                assign_node(parent, node.left, node.val)
            elif node.right:
                assign_node(parent, node.right, node.val)
            else:
                assign_node(parent, None, node.val)
        else:
            root = node.left or node.right

        return root
