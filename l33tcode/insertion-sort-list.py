class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        fake_inf = ListNode(float("-inf"))
        node = head
        prev_node = fake_inf

        while node:
            if prev_node.val > node.val:
                inner_node = head
                inner_prev_node = fake_inf

                while inner_node:
                    if inner_node.val > node.val:
                        if inner_node == head:
                            head = node
                        prev_node.next = node.next
                        inner_prev_node.next = node
                        node.next = inner_node
                        node = prev_node.next
                        break
                    inner_prev_node = inner_node
                    inner_node = inner_node.next
            else:
                prev_node = node
                node = node.next

        return head


x = ListNode(4)
x.next = ListNode(2)
x.next.next = ListNode(1)
x.next.next.next = ListNode(3)

s = Solution()
h = s.insertionSortList(x)

print(h.val)
print(h.next.val)
print(h.next.next.val)
print(h.next.next.next.val)
