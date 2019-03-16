class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head):
        if head is None:
            return None

        head, last = self.reverseListRecursive(head, head)

        return last

    def reverseListRecursive(self, head, last):
        if head.next is not None:
            right, last = self.reverseListRecursive(head.next, head.next)
            right.next = head
            head.next = None

        return head, last

    def reverseListIteratively(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        prev = None

        while node is not None:
            next_node = node.next
            node.next = prev
            prev = node
            node = next_node

        return prev

x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(3)
x.next.next.next = ListNode(4)

sol = Solution()
y = sol.reverseList(x)
print(y.val)
print(y.next.val)
print(y.next.next.val)
print(y.next.next.next.val)
