"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, node):
        if node is None or not node.left and not node.right:
            return node

        if node.left:
            node.left.next = node.right

        if node.next:
            node_without_next = node.right if node.right else node.left
            next_node = node.next
            while next_node:
                if next_node.left:
                    node_without_next.next = next_node.left
                    break
                if next_node.right:
                    node_without_next.next = next_node.right
                    break
                next_node = next_node.next

        self.connect(node.right)
        self.connect(node.left)

        return node

# TODO: come with non-recursive approach
