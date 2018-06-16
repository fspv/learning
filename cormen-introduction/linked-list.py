class DoubleLinkedListNode():
    def __init__(self, key=None):
        self.prev = None
        self.next = None
        self.key = key

class DoubleLinkedList():
    def __init__(self):
        self.nil = DoubleLinkedListNode()
        self.nil.next = self.nil
        self.nil.prev = self.nil

    def insert(self, node):
        self.nil.next.prev = node
        node.next = self.nil.next
        self.nil.next = node
        node.prev = self.nil

    def search(self, key):
        node = self.nil.next
        while node.key != key and node.key != self.nil.key:
            node = node.next

        return node

    def delete(self, key):
        node = self.search(key)
        if node.key != self.nil.key:
            node.prev.next = node.next
            node.next.prev = node.prev

    def __eq__(self, other):
        list_repr = []
        node = self.nil.next

        while node.key != self.nil.key:
            list_repr.append(node.key)
            node = node.next

        return list_repr == other

    def __repr__(self):
        list_repr = []
        node = self.nil.next

        while node.key != self.nil.key:
            list_repr.append(node.key)
            node = node.next

        return str(list_repr)

# Tests
double_linked_list = DoubleLinkedList()
double_linked_list.insert(DoubleLinkedListNode(1))
double_linked_list.insert(DoubleLinkedListNode(4))
double_linked_list.insert(DoubleLinkedListNode(16))
double_linked_list.insert(DoubleLinkedListNode(9))
assert double_linked_list == [9, 16, 4, 1]
double_linked_list.insert(DoubleLinkedListNode(25))
assert double_linked_list == [25, 9, 16, 4, 1]
double_linked_list.delete(1)
assert double_linked_list == [25, 9, 16, 4]

# 10.2-1
class SingleLinkedListNode():
    def __init__(self, key=None):
        self.next = None
        self.key = key

class SingleLinkedList():
    def __init__(self):
        self.nil = SingleLinkedListNode()
        self.nil.next = self.nil

    def insert(self, node):
        node.next = self.nil.next
        self.nil.next = node

    def search(self, key):
        node = self.nil.next
        while node.key != key and node.key != self.nil.key:
            node = node.next

        return node

    def search_prev(self, key):
        node = self.nil.next
        while node.next.key != key and node.key != self.nil.key:
            node = node.next

        return node

    def delete(self, key):
        node = self.search_prev(key)
        if node.next.key != self.nil.key:
            node.next = node.next.next

    def __eq__(self, other):
        list_repr = []
        node = self.nil.next

        while node.key != self.nil.key:
            list_repr.insert(0, node.key)
            node = node.next

        return list_repr == other

    def __repr__(self):
        list_repr = []
        node = self.nil.next

        while node.key != self.nil.key:
            list_repr.insert(0, node.key)
            node = node.next

        return str(list_repr)

# Tests
single_linked_list = SingleLinkedList()
single_linked_list.insert(SingleLinkedListNode(1))
single_linked_list.insert(SingleLinkedListNode(4))
single_linked_list.insert(SingleLinkedListNode(16))
single_linked_list.insert(SingleLinkedListNode(9))
assert single_linked_list == [1, 4, 16, 9]
single_linked_list.insert(SingleLinkedListNode(25))
assert single_linked_list == [1, 4, 16, 9, 25]
single_linked_list.delete(1)
assert single_linked_list == [4, 16, 9, 25]


# 10.2-2
class SingleLinkedListStackOverflowError(BaseException):
    pass


class SingleLinkedListStackUnderflowError(BaseException):
    pass


class SingleLinkedListStack(SingleLinkedList):
    top = 0

    def stack_empty(self):
        return self.top == 0

    def push(self, value):
        self.insert(SingleLinkedListNode(value))
        self.top += 1

    def pop(self):
        if self.nil.next.key == self.nil.key:
            raise SingleLinkedListStackUnderflowError
        else:
            node = self.nil.next
            self.delete(node.key)

        self.top -= 1

        return node.key


# Tests
single_linked_list_stack = SingleLinkedListStack()

assert single_linked_list_stack.stack_empty()

single_linked_list_stack.push(15)
single_linked_list_stack.push(6)
single_linked_list_stack.push(2)
single_linked_list_stack.push(9)

assert single_linked_list_stack == [15, 6, 2, 9]
assert single_linked_list_stack.top == 4

single_linked_list_stack.push(17)
single_linked_list_stack.push(3)

assert single_linked_list_stack == [15, 6, 2, 9, 17, 3]
assert single_linked_list_stack.top == 6

assert single_linked_list_stack.pop() == 3
assert single_linked_list_stack.top == 5

single_linked_list_stack.push(51)

single_linked_list_stack.pop()
single_linked_list_stack.pop()
single_linked_list_stack.pop()
single_linked_list_stack.pop()
single_linked_list_stack.pop()
single_linked_list_stack.pop()

assert single_linked_list_stack.stack_empty()

try:
    single_linked_list_stack.pop()
    raise Exception("We can't go there, stack underflow must be raised")
except SingleLinkedListStackUnderflowError:
    pass

# 10.2-7

single_linked_list_stack = SingleLinkedListStack()

single_linked_list_stack.push(15)
single_linked_list_stack.push(6)
single_linked_list_stack.push(2)
single_linked_list_stack.push(9)

assert single_linked_list_stack == [15, 6, 2, 9]

node = single_linked_list_stack.nil

while True:
    node_prev = node
    if node_prev.key == single_linked_list_stack.nil.key:
        node = node_prev.next
        node_next = node_prev.next.next
    else:
        node = node_next
        node_next = node_next.next
    node.next = node_prev
    if node.key == single_linked_list_stack.nil.key:
        break

assert single_linked_list_stack == [9, 2, 6, 15]
