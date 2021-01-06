from typing import Dict, Optional


class DoubleLinkedListNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.key: Optional[int] = None
        self.frequency: Optional[DoubleLinkedListNode] = None
        self.tail: Optional[DoubleLinkedListNode] = None
        self.next: Optional[DoubleLinkedListNode] = None
        self.prev: Optional[DoubleLinkedListNode] = None


def remove_node(node: DoubleLinkedListNode) -> None:
    prev_node = node.prev
    next_node = node.next
    if prev_node:
        prev_node.next = next_node
    if next_node:
        next_node.prev = prev_node


def insert_after(node: DoubleLinkedListNode, after: DoubleLinkedListNode) -> None:
    prev_node = after
    next_node = after.next

    if prev_node:
        prev_node.next = node

    node.prev = prev_node

    if next_node:
        next_node.prev = node

    node.next = next_node


class LFUCache:
    def __init__(self, capacity: int) -> None:
        self._count: int = 0
        self._capacity: int = capacity
        self._key_map: Dict[int, DoubleLinkedListNode] = {}
        self._head: DoubleLinkedListNode = DoubleLinkedListNode(0)
        self._frequency_head: DoubleLinkedListNode = DoubleLinkedListNode(0)
        self._frequency_head.tail = self._head
        self._head.frequency = self._frequency_head

    def _get_next_freq_or_create(
        self, frequency: DoubleLinkedListNode,
    ) -> DoubleLinkedListNode:
        frequency_next = frequency.next

        if frequency.next and frequency.value + 1 == frequency.next.value:
            pass
        else:
            frequency_next = DoubleLinkedListNode(frequency.value + 1)
            insert_after(frequency_next, frequency)

        if not frequency_next:
            raise ValueError("next frequency is not set")

        return frequency_next

    def _insert_into_frequency(
        self, frequency: DoubleLinkedListNode, node: DoubleLinkedListNode
    ) -> None:
        move_node_after = frequency.tail or frequency.prev.tail
        insert_after(node, move_node_after)
        node.frequency = frequency
        frequency.tail = node

    def _remove_node_with_freq(self, node: DoubleLinkedListNode) -> None:
        frequency = node.frequency

        if not frequency:
            raise ValueError("node should have frequency")

        # Remove node from the list and update the current frequency
        remove_node(node)
        if node == frequency.tail:
            frequency.tail = frequency.tail.prev

        frequency_tail = frequency.tail

        if not frequency_tail:
            raise ValueError("Frequency tail should not be empty at this point")

        if frequency_tail.frequency != frequency:
            remove_node(frequency)

    def touch(self, key: int) -> None:
        node = self._key_map.get(key)

        if not node:
            return

        frequency = node.frequency
        node_prev = node.prev
        node_next = node.next

        if not frequency:
            raise ValueError("Node should always have a frequency")

        # Remove node from the list and update the current frequency
        self._remove_node_with_freq(node)

        # Get or create the next frequency
        frequency_next = self._get_next_freq_or_create(frequency)

        # Insert node into the end of the current frequency
        self._insert_into_frequency(frequency_next, node)

    def get(self, key: int) -> int:
        self.touch(key)

        node = self._key_map.get(key)

        if not node:
            return -1

        return node.value

    def put(self, key: int, value: int) -> None:
        if self._capacity == 0:
            return

        node = self._key_map.get(key)

        if node:
            self.touch(key)
            node.value = value
        else:
            if self._count + 1 > self._capacity:
                self._key_map.pop(self._head.next.key)
                self._remove_node_with_freq(self._head.next)
                self._count -= 1

            node = DoubleLinkedListNode(value)
            node.key = key
            self._key_map[key] = node
            self._insert_into_frequency(self._frequency_head, node)
            self.touch(key)
            self._count += 1
