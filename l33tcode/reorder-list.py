import math
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        def reverse_list(node: Optional[ListNode]) -> Optional[ListNode]:
            prev = None

            while node:
                node_next = node.next
                node.next = prev
                prev = node
                node = node_next

            return prev

        if not head:
            return

        num_nodes = 0
        node = head

        while node:
            num_nodes += 1
            node = node.next

        node = head
        for _ in range(math.ceil(num_nodes / 2) - 1):
            node = node.next

        last = reverse_list(node.next)
        node.next = None
        node = head

        while node and last:
            node_new, last_new = node.next, last.next
            node.next, last.next = last, node.next
            node, last = node_new, last_new
