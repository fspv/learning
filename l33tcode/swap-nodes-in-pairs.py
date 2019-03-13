# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        if head is None or head.next is None:
            return head

        left = head
        right = head.next

        left.next = right.next
        right.next = left

        left.next = self.swapPairs(left.next)

        return right

x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)

s = Solution()
s.swapPairs(x)
