class MyCircularDeque:
    _data: list[int]
    _head: int
    _tail: int
    _count: int

    def __init__(self, k: int):
        self._data = [0] * k
        self._head = 0
        self._tail = 0
        self._count = 0

    def insertFront(self, value: int) -> bool:
        # check is not full
        if self.isFull():
            return False
        # move the head pointer
        self._head -= 1
        self._head %= len(self._data)
        # set the value
        self._data[self._head] = value

        self._count += 1

        return True

    def insertLast(self, value: int) -> bool:
        # check is not full
        if self.isFull():
            return False
        # set the value
        self._data[self._tail] = value
        # move the tail pointer
        self._tail += 1
        self._tail %= len(self._data)

        self._count += 1

        return True

    def deleteFront(self) -> bool:
        # check is not empty
        if self.isEmpty():
            return False
        # move the head pointer
        self._head += 1
        self._head %= len(self._data)

        self._count -= 1

        return True

    def deleteLast(self) -> bool:
        # check is not empty
        if self.isEmpty():
            return False
        # move the tail pointer
        self._tail -= 1
        self._tail %= len(self._data)

        self._count -= 1

        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[self._head]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self._data[(self._tail - 1) % len(self._data)]

    def isEmpty(self) -> bool:
        return self._count == 0

    def isFull(self) -> bool:
        return self._count == len(self._data)


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
