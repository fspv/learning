from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class ListNode:
    val: int
    next: Optional[ListNode]


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head

        while fast:
            slow = slow.next  # type: ignore
            if fast.next:
                fast = fast.next.next
            else:
                fast = None

            if slow and slow == fast:
                return True

        return False
