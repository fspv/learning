class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class ArrayStack():
    top = 0

    def __init__(self, length):
        self._stack_length = length
        self._stack = [None] * length

    def push(self, element):
        if self.top < self._stack_length:
            self._stack[self.top] = element
        else:
            raise StackOverflowError
        self.top += 1

    def pop(self):
        if self.top == 0:
            raise StackUnderflowError
        else:
            element = self._stack[self.top - 1]
            self.top -= 1
            return element

    def stack_empty(self):
        return self.top == 0

    def __eq__(self, other):
        return self._stack[:self.top] == other

    def __repr__(self):
        return str({"top": self.top, "stack": self._stack})


# Tests

array_stack = ArrayStack(7)

assert array_stack.stack_empty()

array_stack.push(15)
array_stack.push(6)
array_stack.push(2)
array_stack.push(9)

assert array_stack == [15, 6, 2, 9]
assert array_stack.top == 4

array_stack.push(17)
array_stack.push(3)

assert array_stack == [15, 6, 2, 9, 17, 3]
assert array_stack.top == 6

assert array_stack.pop() == 3
assert array_stack.top == 5

array_stack.push(51)
array_stack.push(15)
try:
    array_stack.push(666)
    raise Exception("We can't go there, stack overflow must be raised")
except StackOverflowError:
    pass

array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()
array_stack.pop()

assert array_stack.stack_empty()

try:
    array_stack.pop()
    raise Exception("We can't go there, stack underflow must be raised")
except StackUnderflowError:
    pass

# 10.1-1
array_stack = ArrayStack(6)
print(array_stack)
array_stack.push(4)
print(array_stack)
array_stack.push(1)
print(array_stack)
array_stack.pop()
print(array_stack)
array_stack.push(8)
print(array_stack)
array_stack.pop()
print(array_stack)

# 10.1-2
class SharedArrayStack():
    top = 0

    def __init__(self, array_free_positions, array):
        self._array_free_positions = array_free_positions
        self._array = array
        self._array_taken_positions = ArrayStack(len(array))

    def push(self, value):
        if self._array_free_positions.top == 0:
            raise StackOverflowError
        else:
            position = self._array_free_positions.pop()
        self._array[position] = value
        self._array_taken_positions.push(position)

    def pop(self):
        position = self._array_taken_positions.pop()
        value = self._array[position]
        self._array_free_positions.push(position)

        return value


array = [None] * 7
array_free_positions = ArrayStack(len(array))
for pos in range(len(array), 0, -1):
    array_free_positions.push(pos - 1)

shared_array_stack1 = SharedArrayStack(array_free_positions, array)
shared_array_stack2 = SharedArrayStack(array_free_positions, array)

shared_array_stack1.push(1)
shared_array_stack1.push(2)
shared_array_stack1.push(3)

shared_array_stack2.push(4)
shared_array_stack2.push(5)
shared_array_stack2.push(6)
shared_array_stack2.push(7)

try:
    shared_array_stack2.push(8)
    raise Exception("We can't go there, stack overflow must be raised")
except StackOverflowError:
    pass

shared_array_stack1.pop()
shared_array_stack1.pop()
shared_array_stack1.pop()

try:
    shared_array_stack1.pop()
    raise Exception("We can't go there, stack underflow must be raised")
except StackUnderflowError:
    pass
