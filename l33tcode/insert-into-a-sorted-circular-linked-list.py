# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def insert(self, head: "Node", insertVal: int) -> "Node":
        new = Node(insertVal)
        new.next = new

        node = head
        while node:
            if (
                (node.val <= new.val <= node.next.val)
                or (
                    node.val > node.next.val
                    and (node.next.val > new.val or new.val > node.val)
                )
                or node.next == head
            ):
                node.next, new.next = new, node.next
                break
            node = node.next

        return head or new
