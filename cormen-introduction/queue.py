class QueueOverflowError(Exception):
    pass


class QueueUnderflowError(Exception):
    pass


class ArrayQueue():
    head = 0
    tail = 0
    _number_of_elements = 0

    def __init__(self, length):
        self.length = length
        self._queue = [None] * length

    def queue_empty(self):
        return self._number_of_elements == 0

    def queue_full(self):
        return self._number_of_elements == self.length

    def enqueue(self, value):
        new_tail = (self.tail + 1) % self.length

        if self.queue_full():
            raise QueueOverflowError

        self._queue[self.tail] = value

        self.tail = new_tail

        self._number_of_elements += 1

    def dequeue(self):
        new_head = (self.head + 1) % self.length

        if self.queue_empty():
            raise QueueUnderflowError

        value = self._queue[self.head]

        self.head = new_head

        self._number_of_elements -= 1

        return value

    def __eq__(self, other):
        return self._queue_[self.head:self.tail] == other

    def __repr__(self):
        return str({"head": self.head, "tail": self.tail, "queue": self._queue})


array_queue = ArrayQueue(7)

array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)
array_queue.enqueue(4)
array_queue.enqueue(5)
array_queue.enqueue(6)
array_queue.enqueue(7)

try:
    array_queue.enqueue(8)
    raise Exception("We can't go there, queue overderflow must be raised")
except QueueOverflowError:
    pass

assert array_queue.dequeue() == 1
assert array_queue.dequeue() == 2
assert array_queue.dequeue() == 3
assert array_queue.dequeue() == 4
assert array_queue.dequeue() == 5
assert array_queue.dequeue() == 6
assert array_queue.dequeue() == 7

try:
    array_queue.dequeue()
    raise Exception("We can't go there, queue underderflow must be raised")
except QueueUnderflowError:
    pass

array_queue.enqueue(1)
array_queue.enqueue(2)
array_queue.enqueue(3)
array_queue.enqueue(4)
array_queue.enqueue(5)
array_queue.enqueue(6)
array_queue.enqueue(7)
assert array_queue.dequeue() == 1
assert array_queue.dequeue() == 2

array_queue.enqueue(6)
array_queue.enqueue(7)
assert array_queue.dequeue() == 3
assert array_queue.dequeue() == 4
