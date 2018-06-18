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

    def __add__(self, other):
        new_list = DoubleLinkedList()

        new_list.nil.next = self.nil.next
        new_list.nil.prev = other.nil.prev
        self.nil.prev.next = other.nil.next
        other.nil.next.prev = self.nil.prev
        new_list.nil.next.prev = new_list.nil
        new_list.nil.prev.next = new_list.nil

        return new_list


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

# Union 10.2.6
double_linked_list2 = DoubleLinkedList()
double_linked_list2.insert(DoubleLinkedListNode(31))
double_linked_list2.insert(DoubleLinkedListNode(98))
double_linked_list2.insert(DoubleLinkedListNode(132))
double_linked_list2.insert(DoubleLinkedListNode(439))

# This destroys original lists, they can't be used anymore.
# It is the price of O(1) operation complexity, because copy of
# lists is as complex as O(n)
new_list = double_linked_list + double_linked_list2
del double_linked_list
del double_linked_list2

assert new_list == [25, 9, 16, 4, 439, 132, 98, 31]


# 10.2-1
class SingleLinkedListNode():
    def __init__(self, key=None):
        self.next = None
        self.key = key

    def __eq__(self, other):
        return self is other

    def __neq__(self, other):
        return self is not other


class SingleLinkedList():
    def __init__(self):
        self.nil = SingleLinkedListNode()
        self.nil.next = self.nil

    def insert(self, node):
        node.next = self.nil.next
        self.nil.next = node

    def search(self, key):
        node = self.nil.next
        while node.key != key and node != self.nil:
            node = node.next

        return node

    def search_faster(self, key):
        # 10.2-4
        node = self.nil.next
        self.nil.key = key
        while node.key != key:
            node = node.next

        self.nil.key = None

        return node

    def search_prev(self, key):
        node = self.nil.next
        while node.next.key != key and node != self.nil:
            node = node.next

        return node

    def delete(self, key):
        node = self.search_prev(key)
        if node.next != self.nil:
            node.next = node.next.next

    def reverse(self):
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

    def __eq__(self, other):
        list_repr = []
        node = self.nil.next

        while node != self.nil:
            list_repr.insert(0, node.key)
            node = node.next

        return list_repr == other

    def __repr__(self):
        list_repr = []
        node = self.nil.next

        while node != self.nil:
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


# 10.2-2
class SingleLinkedListQueueOverflowError(BaseException):
    pass


class SingleLinkedListQueueUnderflowError(BaseException):
    pass


class SingleLinkedListQueue(SingleLinkedList):
    def __init__(self, length):
        super(SingleLinkedListQueue, self).__init__()
        self.length = length
        self.size = 0
        self.head = self.nil
        self.tail = self.nil

    def queue_empty(self):
        return self.head == self.tail

    def queue_full(self):
        return self.size == self.length

    def enqueue(self, value):
        if self.queue_full():
            raise SingleLinkedListQueueOverflowError
        else:
            node = SingleLinkedListNode(value)
            node.next = self.nil
            self.tail.next = node
            self.tail = node
            self.size += 1

    def dequeue(self):
        if self.queue_empty():
            raise SingleLinkedListQueueUnderflowError
        else:
            value = self.head.next.key
            if self.head.next == self.tail:
                self.tail = self.head
            self.delete(self.head.next.key)
            self.size -= 1
            return value


single_linked_list_queue = SingleLinkedListQueue(7)

single_linked_list_queue.enqueue(1)
single_linked_list_queue.enqueue(2)
single_linked_list_queue.enqueue(3)
single_linked_list_queue.enqueue(4)
single_linked_list_queue.enqueue(5)
single_linked_list_queue.enqueue(6)
single_linked_list_queue.enqueue(7)

try:
    single_linked_list_queue.enqueue(8)
    raise Exception("We can't go there, queue overderflow must be raised")
except SingleLinkedListQueueOverflowError:
    pass

assert single_linked_list_queue.dequeue() == 1
assert single_linked_list_queue.dequeue() == 2
assert single_linked_list_queue.dequeue() == 3
assert single_linked_list_queue.dequeue() == 4
assert single_linked_list_queue.dequeue() == 5
assert single_linked_list_queue.dequeue() == 6
assert single_linked_list_queue.dequeue() == 7

try:
    single_linked_list_queue.dequeue()
    raise Exception("We can't go there, queue underderflow must be raised")
except SingleLinkedListQueueUnderflowError:
    pass

single_linked_list_queue.enqueue(1)
single_linked_list_queue.enqueue(2)
single_linked_list_queue.enqueue(3)
single_linked_list_queue.enqueue(4)
single_linked_list_queue.enqueue(5)
single_linked_list_queue.enqueue(6)
single_linked_list_queue.enqueue(7)
assert single_linked_list_queue.dequeue() == 1
assert single_linked_list_queue.dequeue() == 2

single_linked_list_queue.enqueue(6)
single_linked_list_queue.enqueue(7)
assert single_linked_list_queue.dequeue() == 3
assert single_linked_list_queue.dequeue() == 4


# 10.2-7

single_linked_list_stack = SingleLinkedListStack()

single_linked_list_stack.push(15)
single_linked_list_stack.push(6)
single_linked_list_stack.push(2)
single_linked_list_stack.push(9)

assert single_linked_list_stack == [15, 6, 2, 9]

single_linked_list_stack.reverse()

assert single_linked_list_stack == [9, 2, 6, 15]
