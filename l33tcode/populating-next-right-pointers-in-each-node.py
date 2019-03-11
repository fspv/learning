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
        if node.next:
            node.right.next = node.next.left
        node.left.next = node.right
        self.connect(node.left)
        self.connect(node.right)

        return node

# TODO: come with non-recursive approach
