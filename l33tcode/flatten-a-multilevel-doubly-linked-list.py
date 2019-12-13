"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        stack = [None]

        node = head

        while stack:
            while node:
                node_prev = node

                if node.child:
                    stack.append(node.next)
                    node.next = node.child
                    node.child.prev = node
                    node.child = None

                node = node.next

            right = stack.pop()

            if right:
                node_prev.next = right
                right.prev = node_prev
                node = right

        return head


    def flatten_recursive(self, head: 'Node') -> 'Node':
        def dive(left, node, right):
            if left:
                node.prev = left
                left.next = node
                left.child = None

            while node:
                node_prev, node_next = node, node.next

                if node.child:
                    dive(node, node.child, node.next)

                node = node_next

            if right:
                node_prev.next = right
                right.prev = node_prev

        dive(None, head, None)

        return head
