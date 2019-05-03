# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq

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

        return root.next
