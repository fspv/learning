from typing import Optional


class Number:
    def __init__(self, node: Optional[ListNode]) -> None:
        self.head = node

    def reverse(self) -> None:
        node = None
        next_node = self.head

        while next_node:
            next_node.next, next_node, node = node, next_node.next, next_node

        self.head = node

    def __add__(self, other: "Number") -> "Number":
        self.reverse()
        other.reverse()
        left = self.head
        right = other.head
        head = ListNode(123)

        node = head
        carry = 0
        while left and right:
            node.next = ListNode((left.val + right.val + carry) % 10)
            carry = (left.val + right.val + carry) // 10
            node = node.next
            left = left.next
            right = right.next

        while left:
            node.next = ListNode((left.val + carry) % 10)
            carry = (left.val + carry) // 10
            node = node.next
            left = left.next

        while right:
            node.next = ListNode((right.val + carry) % 10)
            carry = (right.val + carry) // 10
            node = node.next
            right = right.next

        if carry > 0:
            node.next = ListNode(carry)

        self.reverse()
        other.reverse()

        result = Number(head.next)
        result.reverse()

        return result


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        return (Number(l1) + Number(l2)).head
