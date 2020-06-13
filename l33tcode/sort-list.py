from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        def merge(start, left, right, length: int):
            new_head, new_tail = None, None
            ptr_left, ptr_right = left, right
            while ptr_left or ptr_right:
                if ptr_left and (
                    (not ptr_right) or (ptr_right and ptr_left.val < ptr_right.val)
                ):
                    start.next, start, ptr_left = ptr_left, ptr_left, ptr_left.next
                else:
                    start.next, start, ptr_right = ptr_right, ptr_right, ptr_right.next

            return start

        def cut_sublist_from_here(node: ListNode, nodes: int) -> ListNode:
            for _ in range(nodes - 1):
                if node:
                    node = node.next

            node_next = node.next if node else None

            if node:
                node.next = None

            return node_next

        total = 0
        node = head
        while node:
            total += 1
            node = node.next

        power = 0
        cur_head = head
        while (length := 2 ** power) < total:
            node, cur_head = cur_head, None
            start = ListNode()
            prev = start

            while node:
                left = node
                right = cut_sublist_from_here(left, length)
                node = cut_sublist_from_here(right, length)
                prev = merge(prev, left, right, length)

            cur_head = start.next

            power += 1

        return cur_head


node = ListNode(4)
node.next = ListNode(2)
node.next.next = ListNode(1)
node.next.next.next = ListNode(3)

sol = Solution()
sol.sortList(node)
