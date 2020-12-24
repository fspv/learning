from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution2:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        head_left = head
        head_right = head.next

        node_left, node_right = head_left, head_right

        while node_left and node_right:
            node_next_left = node_left.next.next
            node_next_right = node_right.next.next if node_right.next else None

            node_left.next = node_next_left
            node_right.next = node_next_right

            node_left = node_next_left
            node_right = node_next_right

        head_left, head_right = head_right, head_left

        node_left, node_right = head_left, head_right

        while node_left and node_right:
            node_left_next = node_left.next
            node_right_next = node_right.next
            node_left.next, node_right.next = (
                node_right,
                node_left.next or node_right.next,
            )
            node_left = node_left_next
            node_right = node_right_next

        return head_left or head_right


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
