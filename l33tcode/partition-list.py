from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    @dataclass
    class ListNode:
        val: int = 0
        next: Optional[ListNode] = None

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = ListNode()
        left_tail = left_head

        right_head = ListNode()
        right_tail = right_head

        node = head

        while node:
            if node.val < x:
                left_tail.next = node
                left_tail = node
            else:
                right_tail.next = node
                right_tail = node

            node.next, node = None, node.next

        left_tail.next = right_head.next

        return left_head.next
