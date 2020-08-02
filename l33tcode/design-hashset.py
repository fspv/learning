class LinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._hashset = [None] * 10000

    def _hash(self, key: int) -> int:
        return key % len(self._hashset)  # hash(val) - other option

    def add(self, key: int) -> None:
        if self.contains(key):
            return

        new_node = LinkedListNode(key)
        node = self._hashset[self._hash(key)]

        if node:
            while node.next:
                node = node.next

            node.next = new_node
        else:
            self._hashset[self._hash(key)] = new_node

    def remove(self, key: int) -> None:
        node = self._hashset[self._hash(key)]

        if node:
            prev_node, cur_node, next_node = None, node, node.next

            while cur_node and cur_node.val != key:
                prev_node, cur_node = cur_node, next_node
                next_node = cur_node.next if cur_node else None

            if prev_node:
                prev_node.next = next_node
            else:
                self._hashset[self._hash(key)] = next_node

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        node = self._hashset[self._hash(key)]

        if node:
            while node:
                if node.val == key:
                    return True
                node = node.next

        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
