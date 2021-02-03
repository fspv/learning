# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                fast = None

            if slow and slow == fast:
                return True

        return False
