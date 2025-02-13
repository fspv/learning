# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return

        pre_head = ListNode(None)
        pre_head.next = head

        left, right = pre_head, head

        pos = 1

        while right.next:
            if pos >= n:
                left = left.next

            right = right.next
            pos += 1

        left.next = left.next.next

        return pre_head.next
