# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None

        middle, tail = head, head

        while tail:
            if tail and tail.next and tail.next.next:
                tail = tail.next.next
            elif tail and tail.next:
                return middle.next
            elif tail:
                return middle

            middle = middle.next
