# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head

        slow_count = 0

        # Detect cycle
        while slow and fast:
            slow = slow.next
            slow_count += 1

            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None

            if slow == fast:
                break

        # Find beginning
        first, second = head, fast

        while first != second:
            first = first.next
            second = second.next

        return first
