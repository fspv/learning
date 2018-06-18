from linked_list import DoubleLinkedListNode, DoubleLinkedList

class OutOfSpaceMultipleArrayListRepresentationError(BaseException):
    pass

class MultipleArrayListRepresentationNode(list):
    def __init__(self, *args, **kwargs):
        super(MultipleArrayListRepresentationNode, self).__init__(*args, **kwargs)
        self.append(None)
        self.append(None)
        self.append(None)

    @property
    def key(self):
        return self[0]

    @key.setter
    def key(self, value):
        self[0] = value

    @property
    def next(self):
        return self[1]

    @next.setter
    def next(self, value):
        self[1] = value

    @property
    def prev(self):
        return self[2]

    @prev.setter
    def prev(self, value):
        self[2] = value

class MultipleArrayListRepresentation():
    def __init__(self, length):
        # Initialize container
        self.container = []
        for pos in range(length):
            self.container.append(MultipleArrayListRepresentationNode())
            self.get(pos).next = pos + 1 if pos < (length - 1) else None

        # Set nil position
        self.nil_position = 0
        self.nil.next = self.nil_position
        self.nil.prev = self.nil_position

        # Set free_position to the next element
        self.free_position = 1

    def get(self, position):
        return self.container[position]

    @property
    def nil(self):
        return self.container[self.nil_position]

    @property
    def free(self):
        return self.container[self.free_position]

    def allocate_object(self):
        if self.free_position is not None:
            position = self.free_position
            self.free_position = self.free.next
            return position
        else:
            raise OutOfSpaceMultipleArrayListRepresentationError

    def free_object(self, position):
        self.container[self.free_position].next = position
        self.container[position].next = None
        self.free_position = position

    def insert(self, value):
        # allocate
        position = self.allocate_object()
        node = self.get(position)
        node.key = value

        # insert
        nil_next = self.get(self.nil.next)
        nil_next.prev = position
        node.next = self.nil.next
        self.nil.next = position
        node.prev = self.nil_position

    def delete(self, value):
        pass

    def __repr__(self):
        return str(self.container)


multiple_array_list_representation = MultipleArrayListRepresentation(7)
multiple_array_list_representation.insert(978)
multiple_array_list_representation.insert(123)
multiple_array_list_representation.insert(123)
multiple_array_list_representation.insert(123)
multiple_array_list_representation.insert(123)
multiple_array_list_representation.insert(123)
try:
    multiple_array_list_representation.insert(123)
    raise Exception("We can't go there, out of space must be raised")
except OutOfSpaceMultipleArrayListRepresentationError:
    pass

#assert multiple_array_list_representation == [[None, 6, 1], [978, 0, 2], [123, 1, 3], [123, 2, 4], [123, 3, 5], [123, 4, 6], [123, 5, 0]]
