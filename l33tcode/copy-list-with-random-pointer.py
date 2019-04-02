"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if head is None:
            return

        mem = {}

        def node_copy(node):
            if node is None:
                return

            if node in mem:
                return mem[node]

            mem[node] = Node(node.val, None, None)
            mem[node].next = node_copy(node.next)
            mem[node].random = node_copy(node.random)

            return mem[node]

        return node_copy(head)
