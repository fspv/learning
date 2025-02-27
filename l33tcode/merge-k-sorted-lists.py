# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
from typing import List


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap = []

        count = 0

        for node in lists:
            if node is not None:
                count += 1
                heapq.heappush(heap, (node.val, count, node))

        root = ListNode(None)

        node = root

        while True:
            count += 1
            if not heap:
                break

            min_node_val, c, min_node = heapq.heappop(heap)

            node.next = min_node
            node = node.next

            if min_node.next is not None:
                heapq.heappush(heap, (min_node.next.val, count, min_node.next))


# Definition for singly-linked list.
class ListNodeComparable:
    def __init__(self, node: ListNode):
        self.val = node.val
        self.next = node.next
        self.node = node

    def __eq__(self, other: object) -> bool:
        return self.val == other.val

    def __lt__(self, other: object) -> bool:
        return self.val < other.val


class Solution2:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        heap: List[ListNodeComparable] = []

        head = ListNode()

        for node in lists:
            if node:
                heapq.heappush(heap, ListNodeComparable(node))

        node = head
        while heap:
            cur_node = heapq.heappop(heap)

            if cur_node.next:
                heapq.heappush(heap, ListNodeComparable(cur_node.next))

            node.next = cur_node.node
            node = node.next

        return head.next
