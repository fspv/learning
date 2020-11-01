# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        number = 0

        node = head
        while node:
            number <<= 1
            number |= node.val
            node = node.next

        return number
