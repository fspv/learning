# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        fake_head = ListNode()
        fake_head.next = head

        left, middle = fake_head, fake_head.next

        while middle:
            while middle and middle.next and middle.val == middle.next.val:
                right = middle.next

                while middle and middle.val == right.val:
                    middle = middle.next

                left.next = middle

            if not middle:
                break

            left, middle = middle, middle.next

        return fake_head.next
