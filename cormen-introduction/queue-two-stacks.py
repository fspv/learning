from stack import ArrayStack, StackOverflowError, StackUnderflowError

class TwoStackQueue():
    def __init__(self, length):
        self.stack_first = ArrayStack(length)
        self.stack_second = ArrayStack(length)

    def enqueue(self, value):
        self.stack_first.push(value)

    def dequeue(self):
        while self.stack_first.top != 0:
            self.stack_second.push(self.stack_first.pop())

        value = self.stack_second.pop()

        while self.stack_second.top != 0:
            self.stack_first.push(self.stack_second.pop())

        return value


two_stack_queue = TwoStackQueue(7)

two_stack_queue.enqueue(1)
two_stack_queue.enqueue(2)
two_stack_queue.enqueue(3)
two_stack_queue.enqueue(4)
two_stack_queue.enqueue(5)
two_stack_queue.enqueue(6)
two_stack_queue.enqueue(7)

try:
    two_stack_queue.enqueue(8)
    raise Exception("We can't go there, stack overderflow must be raised")
except StackOverflowError:
    pass

assert two_stack_queue.dequeue() == 1
assert two_stack_queue.dequeue() == 2
assert two_stack_queue.dequeue() == 3
assert two_stack_queue.dequeue() == 4
assert two_stack_queue.dequeue() == 5
assert two_stack_queue.dequeue() == 6
assert two_stack_queue.dequeue() == 7

try:
    two_stack_queue.dequeue()
    raise Exception("We can't go there, stack underderflow must be raised")
except StackUnderflowError:
    pass

two_stack_queue.enqueue(1)
two_stack_queue.enqueue(2)
two_stack_queue.enqueue(3)
two_stack_queue.enqueue(4)
two_stack_queue.enqueue(5)
two_stack_queue.enqueue(6)
two_stack_queue.enqueue(7)
assert two_stack_queue.dequeue() == 1
assert two_stack_queue.dequeue() == 2

two_stack_queue.enqueue(6)
two_stack_queue.enqueue(7)
assert two_stack_queue.dequeue() == 3
assert two_stack_queue.dequeue() == 4

