class DoublyLinkedListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.container = {}
        self.min = DoublyLinkedListNode(None)
        self.max = DoublyLinkedListNode(None)
        self.min.next = self.max
        self.max.prev = self.min

    def _remove_node(self, node):
        """Remove node from its current position"""
        node_prev = node.prev
        node_next = node.next
        node_prev.next = node_next
        node_next.prev = node_prev

    def _add_node_before(self, node, node_next):
        """Add node before the given one"""
        node_prev = node_next.prev
        node_prev.next = node
        node.prev = node_prev
        node_next.prev = node
        node.next = node_next

    def get(self, key: int) -> int:
        """Get node value and update its access time"""
        if key not in self.container:
            return -1

        node = self.container[key]
        self._remove_node(node)
        self._add_node_before(node, self.max)

        return node.val[1]

    def put(self, key: int, value: int) -> None:
        """Add additional node to the cache"""
        if key in self.container:
            self.container[key].val = (key, value)
            self.get(key)
            return

        if self.capacity == 0:
            return -1

        if len(self.container) == self.capacity:
            self.container.pop(self.min.next.val[0])
            self._remove_node(self.min.next)

        node = DoublyLinkedListNode((key, value))
        self._add_node_before(node, self.max)
        self.container[key] = node


cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1
cache.put(3, 3)
assert cache.get(2) == -1
cache.put(4, 4)
assert cache.get(1) == -1
assert cache.get(3) == 3
assert cache.get(4) == 4
