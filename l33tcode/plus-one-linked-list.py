# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return ListNode(1)

        def reverse_list(head: ListNode) -> ListNode:
            prev, cur = head, head.next
            prev.next = None

            new_head = prev

            while cur:
                new_head = cur
                cur_next = cur.next
                cur.next = prev
                prev, cur = cur, cur_next

            return new_head

        new_head = reverse_list(head)

        node = new_head

        carry = 1
        while node and carry > 0:
            node.val, carry = (node.val + carry) % 10, (node.val + carry) // 10
            node = node.next

        new_head = reverse_list(new_head)

        if carry > 0:
            carry_head = ListNode(1)
            carry_head.next = new_head
            new_head = carry_head

        return new_head
