from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(
        self, head_a: ListNode, head_b: ListNode
    ) -> Optional[ListNode]:
        length_a, length_b = 0, 0

        node_a, node_b = head_a, head_b
        while node_a:
            node_a = node_a.next
            length_a += 1

        while node_b:
            node_b = node_b.next
            length_b += 1

        if length_a > length_b:
            node_a, node_b = head_a, head_b
        else:
            node_b, node_a = head_a, head_b

        for _ in range(abs(length_a - length_b)):
            node_a = node_a.next

        while (node_a or node_b) and node_a != node_b:
            node_a = node_a.next
            node_b = node_b.next

        if node_a and node_b:
            return node_a

        return None
