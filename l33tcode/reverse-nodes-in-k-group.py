from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_k(node: Optional[ListNode]) -> Optional[ListNode]:
            if not node:
                return None

            # If left less than k - do not reverse
            cur_node = node

            for _ in range(k):
                if not cur_node:
                    return node

                cur_node = cur_node.next

            # Reverse
            cur_node = node
            prev_node = None

            for _ in range(k):
                prev_node, cur_node.next, cur_node = cur_node, prev_node, cur_node.next

            node.next = reverse_k(cur_node)

            return prev_node

        return reverse_k(head)
