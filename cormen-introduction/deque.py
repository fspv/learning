from queue import ArrayQueue, QueueOverflowError, QueueUnderflowError

class Deque(ArrayQueue):
    def push_back(self, value):
        self.enqueu(value)

    def pop_back(self):
        return self.dequeue()

    def push_front(self, value):
        new_head = (self.length + self.head - 1) % self.length

        if self.queue_full():
            raise QueueOverflowError

        self.head = new_head

        self._queue[self.head] =  value

        self._number_of_elements += 1

    def pop_front(self):
        new_head = (self.length + self.head + 1) % self.length

        if self.queue_empty():
            raise QueueUnderflowError

        value = self._queue[self.head]

        self.head = new_head

        self._number_of_elements -= 1

        return value


# Tests

deque = Deque(7)

deque.push_front(1)
deque.push_front(2)
deque.push_front(3)
deque.push_front(4)
deque.push_front(5)
deque.push_front(6)
deque.push_front(7)

try:
    deque.push_front(8)
    raise Exception("We can't go there, queue overderflow must be raised")
except QueueOverflowError:
    pass

assert deque.pop_front() == 7
assert deque.pop_front() == 6
assert deque.pop_front() == 5
assert deque.pop_front() == 4
assert deque.pop_front() == 3
assert deque.pop_front() == 2
assert deque.pop_front() == 1

try:
    deque.pop_front()
    raise Exception("We can't go there, queue underderflow must be raised")
except QueueUnderflowError:
    pass

deque.push_front(1)
deque.push_front(2)
deque.push_front(3)
deque.push_front(4)
deque.push_front(5)
deque.push_front(6)
deque.push_front(7)
assert deque.pop_front() == 7
assert deque.pop_front() == 6

deque.push_front(6)
deque.push_front(7)
assert deque.pop_front() == 7
assert deque.pop_front() == 6
