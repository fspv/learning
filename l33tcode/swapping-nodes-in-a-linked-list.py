# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        def get_length(head: ListNode) -> int:
            node = head
            length = 0

            while node:
                node = node.next
                length += 1

            return length

        def get_node(head: ListNode, pos: int) -> ListNode:
            node = head

            while node and pos > 0:
                node = node.next
                pos -= 1

            return node

        new_head = ListNode()
        new_head.next = head

        length = get_length(head)

        if k > length:
            raise ValueError(f"No node {k} in the list")

        node1_prev = get_node(new_head, k - 1)
        node2_prev = get_node(new_head, length - k)

        node1, node2 = node1_prev.next, node2_prev.next
        node1_next, node2_next = node1.next, node2.next

        if node1 != node2_next:
            node1_prev.next = node2
        else:
            node1.next = node2
        if node2 != node1_next:
            node2.next = node1_next
        else:
            node2.next = node1
        if node2_prev != node1:
            node2_prev.next = node1
        if node1 != node2_next:
            node1.next = node2_next

        return new_head.next
