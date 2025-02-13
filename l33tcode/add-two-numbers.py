from __future__ import annotations
from dataclasses import dataclass


@dataclass
class ListNode:
    val: int
    next: ListNode | None = None


class Solution:
    def addTwoNumbers(
        self,
        l1: ListNode | None,
        l2: ListNode | None,
    ) -> ListNode | None:
        if l1 is None:
            return l2

        if l2 is None:
            return l1

        ptr1, ptr2 = l1, l2
        result = ListNode(0)
        prev = result
        carry = 0

        while ptr1 or ptr2 or carry:
            val1 = ptr1.val if ptr1 else 0
            val2 = ptr2.val if ptr2 else 0

            val_sum = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10

            prev.next = ListNode(val_sum)
            prev = prev.next

            ptr1 = ptr1.next if ptr1 else None
            ptr2 = ptr2.next if ptr2 else None

        return result.next
