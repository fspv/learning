# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        nodes = 1
        node = head
        while node.next:
            nodes += 1
            node = node.next

        node.next = head
        skip = (nodes - k) % nodes

        for _ in range(skip):
            node = node.next

        node_next = node.next

        node.next = None

        return node_next
