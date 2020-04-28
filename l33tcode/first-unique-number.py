class LinkedListNode:
    def __init__(self, val: int):
        self.val = val
        self.prev = None
        self.next = None


class FirstUnique:

    def __init__(self, nums: List[int]):
        self._queue_map = {}
        self._queue_begin = LinkedListNode(None)
        self._queue_end = LinkedListNode(None)
        self._queue_begin.next = self._queue_end
        self._queue_end.prev = self._queue_begin
        self._all = set()

        for num in nums:
            self.add(num)


    def showFirstUnique(self) -> int:
        return self._queue_begin.next.val or -1

    def add(self, value: int) -> None:
        if value in self._queue_map:
            node = self._queue_map[value]
            node.prev.next = node.next
            node.next.prev = node.prev
            del self._queue_map[value]
        elif value not in self._all:
            self._all.add(value)
            new_node = LinkedListNode(value)
            new_node.prev = self._queue_end.prev
            new_node.next = self._queue_end
            self._queue_end.prev.next = new_node
            self._queue_end.prev = new_node
            self._queue_map[value] = new_node


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
