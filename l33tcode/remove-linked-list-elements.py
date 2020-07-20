# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur, prev = head, None
        new_head = None

        while cur:
            if cur.val == val:
                if prev:
                    prev.next = cur.next
            else:
                if not new_head:
                    new_head = cur
                prev = cur
            cur = cur.next

        return new_head
