# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        if head is None:
            return []

        result = []
        stack = []
        node = head
        pos = 0

        while node:
            if stack and stack[-1][0].val < node.val:
                prev_node, prev_pos = stack.pop()
                result[prev_pos] = node.val
                continue
            result.append(0)
            stack.append((node, pos))
            pos += 1
            node = node.next

        return result
