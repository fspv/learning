from __future__ import annotations

from dataclasses import dataclass
from typing import List, Optional


@dataclass
class ListNode:
    val: int
    next: Optional[ListNode] = None


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        def get_length(node: Optional[ListNode]) -> int:
            return get_length(node.next) + 1 if node else 0

        length: int = get_length(head)
        result: List[Optional[ListNode]] = [None] * k

        part_length = length // k
        extra = length % k

        node = head

        for part in range(k):
            result[part] = node
            prev = node

            for _ in range(part_length + (1 if extra > 0 else 0)):
                # `node.next` is guaranteed to exist by the length calculations
                # above
                prev, node = node, node.next  # type: ignore

            if extra > 0:
                extra -= 1

            if prev:
                prev.next = None

        return result
