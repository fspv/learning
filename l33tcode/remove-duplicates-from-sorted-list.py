# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return

        node = head
        prev_node = None

        while node:
            if prev_node and prev_node.val == node.val:
                prev_node.next = node.next
            else:
                prev_node = node

            node = node.next

        return head
