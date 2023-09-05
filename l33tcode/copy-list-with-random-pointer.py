from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class Node:
    val: int
    next: Optional[Node] = None
    random: Optional[Node] = None


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if head is None:
            return

        mem: Dict[Node, Node] = {}

        def node_copy(node: Optional[Node]) -> Optional[Node]:
            if node is None:
                return

            if node in mem:
                return mem[node]

            mem[node] = Node(node.val, None, None)
            mem[node].next = node_copy(node.next)
            mem[node].random = node_copy(node.random)

            return mem[node]

        return node_copy(head)


class Solution2:
    def copyRandomList(self, head: Node) -> Node:
        def get_node(head: Node, pos: int) -> Optional[Node]:
            node = head
            for _ in range(pos):
                if node:
                    node = node.next

            return node

        def get_pos(node: Node) -> int:
            pos = 0

            while node.next:
                node = node.next
                pos += 1

            return pos

        def copy_list(head: Node) -> Node:
            new_head = Node(head.val)
            new_node = new_head

            node = head.next
            while node:
                new_node.next = Node(node.val)
                node = node.next
                new_node = new_node.next

            return new_head

        if not head:
            return head

        new_head = copy_list(head)
        new_length = get_pos(head)
        new_node: Node = new_head
        node: Node = head

        while new_node:
            if node.random:
                pos = get_pos(node.random)
                new_node.random = get_node(new_head, new_length - pos)

            node = node.next  # type: ignore
            new_node = new_node.next  # type: ignore

        return new_head
