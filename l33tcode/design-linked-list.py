from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Node:
    val: int
    next: Node | None = None
    prev: Node | None = None


def _insert_after_node(node: Node, insert_node: Node) -> None:
    prev_node, next_node = node, node.next

    # pointers are always set, because we use dummy values
    if not next_node:
        raise RuntimeError("bug")

    insert_node.prev = prev_node
    insert_node.next = next_node
    prev_node.next = insert_node
    next_node.prev = insert_node


def _delete_after_node(node: Node) -> None:
    prev_node, next_node = node, node.next

    # pointers are always set, because we use dummy values
    if not next_node:
        raise RuntimeError("bug")

    next_next_node = next_node.next

    # pointers are always set, because we use dummy values
    if not next_next_node:
        raise RuntimeError("bug")

    prev_node.next = next_next_node
    next_next_node.prev = prev_node


def _get_node_by_index(node: Node, index: int) -> Node:
    for _ in range(index + 1):
        next_node = node.next
        if not next_node:
            raise RuntimeError("bug")

        node = next_node

    return node


def _get_prev_node_by_index(node: Node, index: int) -> Node:
    for _ in range(index):
        next_node = node.next
        if not next_node:
            raise RuntimeError("bug")

        node = next_node

    return node


class MyLinkedList:
    _head: Node
    _tail: Node
    _count: int

    def __init__(self) -> None:
        self._head = Node(-1)  # dummy node
        self._tail = Node(-1)  # dummy node
        self._head.next = self._tail
        self._tail.prev = self._head
        self._count = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self._count:
            return -1
        return _get_node_by_index(self._head, index).val

    def addAtHead(self, val: int) -> None:
        _insert_after_node(self._head, Node(val))
        self._count += 1

    def addAtTail(self, val: int) -> None:
        if prev := self._tail.prev:
            _insert_after_node(prev, Node(val))
            self._count += 1
            return

        raise RuntimeError("bug")

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self._count:
            return
        node = _get_prev_node_by_index(self._head, index)
        _insert_after_node(node, Node(val))
        self._count += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self._count:
            return

        node = _get_prev_node_by_index(self._head, index)
        _delete_after_node(node)
        self._count -= 1
