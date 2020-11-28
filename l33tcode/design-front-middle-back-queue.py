from typing import Optional


class ListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next: Optional[ListNode] = None
        self.prev: Optional[ListNode] = None


class FrontMiddleBackQueue:
    def __init__(self):
        self.head = ListNode(-123)
        self.tail = ListNode(123)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.middle = self.tail
        self.nodes = 2

    def pushFront(self, val: int) -> None:
        node = ListNode(val)

        head_next = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = head_next
        head_next.prev = node

        self.nodes += 1

        if self.nodes % 2 == 1:
            self.middle = self.middle.prev

    def pushMiddle(self, val: int) -> None:
        node = ListNode(val)

        prev = self.middle.prev

        prev.next = node
        node.prev = prev

        node.next = self.middle
        self.middle.prev = node

        self.nodes += 1

        if self.nodes % 2 == 1:
            self.middle = self.middle.prev

    def pushBack(self, val: int) -> None:
        node = ListNode(val)

        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node

        self.nodes += 1

        if self.nodes % 2 == 0:
            self.middle = self.middle.next

        if self.nodes == 3:
            self.middle = node

    def popFront(self) -> int:
        if self.nodes < 3:
            return -1

        value = self.head.next.val

        tmp = self.head.next.next
        self.head.next = tmp
        tmp.prev = self.head

        self.nodes -= 1

        if self.nodes % 2 == 0:
            self.middle = self.middle.next

        return value

    def popMiddle(self) -> int:
        if self.nodes < 3:
            return -1

        middle = self.middle if self.nodes % 2 == 1 else self.middle.prev

        prev_node = middle.prev
        next_node = middle.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self.middle = middle.next

        self.nodes -= 1

        return middle.val

    def popBack(self) -> int:
        if self.nodes < 3:
            return -1

        if self.nodes == 3:
            return self.popMiddle()

        value = self.tail.prev.val

        tmp = self.tail.prev.prev
        tmp.next = self.tail
        self.tail.prev = tmp

        self.nodes -= 1

        if self.nodes % 2 == 1:
            self.middle = self.middle.prev

        return value


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val) # obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
