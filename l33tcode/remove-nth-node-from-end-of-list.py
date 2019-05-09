# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return

        n = n - 1

        pre_head = ListNode(None)
        left = pre_head
        left.next = right = head
        left_pos = -1
        right_pos = 0

        while right.next:
            if right_pos - left_pos > n:
                left_pos += 1
                left = left.next

            right_pos += 1
            right = right.next

        if right_pos - left_pos == n + 1:
            left.next = left.next.next

        return pre_head.next
