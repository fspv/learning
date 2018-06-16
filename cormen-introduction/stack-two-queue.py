from queue import ArrayQueue, QueueOverflowError, QueueUnderflowError

class TwoQueueStack():
    top = 0

    def __init__(self, length):
        self._queue_first = ArrayQueue(length)
        self._queue_second = ArrayQueue(length)
        self._active_queue = self._queue_first
        self._passive_queue = self._queue_second

    def stack_empty(self):
        return self._active_queue.queue_empty()

    def push(self, value):
        self._active_queue.enqueue(value)
        self.top += 1

    def pop(self):
        value = None

        while True:
            value = self._active_queue.dequeue()
            if self._active_queue.queue_empty():
                break
            else:
                self._passive_queue.enqueue(value)

        self.top -= 1

        active_tmp = self._active_queue
        self._active_queue = self._passive_queue
        self._passive_queue = active_tmp

        return value

    @property
    def _stack(self):
        tmp_array = []
        while not self.stack_empty():
            tmp_array.insert(0, self.pop())

        for value in tmp_array:
            self.push(value)

        return tmp_array

    def __eq__(self, other):
        return self._stack == other

    def __repr__(self):
        return str({"top": self.top, "stack": self._stack})


# Tests

two_queue_stack = TwoQueueStack(7)

assert two_queue_stack.stack_empty()

two_queue_stack.push(15)
two_queue_stack.push(6)
two_queue_stack.push(2)
two_queue_stack.push(9)

assert two_queue_stack == [15, 6, 2, 9]
assert two_queue_stack.top == 4

two_queue_stack.push(17)
two_queue_stack.push(3)

assert two_queue_stack == [15, 6, 2, 9, 17, 3]
assert two_queue_stack.top == 6

assert two_queue_stack.pop() == 3
assert two_queue_stack.top == 5

two_queue_stack.push(51)
two_queue_stack.push(15)
try:
    two_queue_stack.push(666)
    raise Exception("We can't go there, stack overflow must be raised")
except QueueOverflowError:
    pass

two_queue_stack.pop()
two_queue_stack.pop()
two_queue_stack.pop()
two_queue_stack.pop()
two_queue_stack.pop()
two_queue_stack.pop()
two_queue_stack.pop()

assert two_queue_stack.stack_empty()

try:
    two_queue_stack.pop()
    raise Exception("We can't go there, stack underflow must be raised")
except QueueUnderflowError:
    pass

# 10.1-1
two_queue_stack = TwoQueueStack(6)
two_queue_stack.push(4)
two_queue_stack.push(1)
two_queue_stack.pop()
two_queue_stack.push(8)
two_queue_stack.pop()
