# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode()
        left_tail = left_head

        right_head = ListNode()
        right_tail = right_head

        node = head

        while node:
            if node.val < x:
                left_tail.next = node
                left_tail = node
            else:
                right_tail.next = node
                right_tail = node

            node.next, node = None, node.next

        left_tail.next = right_head.next

        return left_head.next
