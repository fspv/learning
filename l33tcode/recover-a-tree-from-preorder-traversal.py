from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    @dataclass
    class TreeNode:
        val: int
        left: TreeNode | None = None
        right: TreeNode | None = None


class Solution:
    def recoverFromPreorder(self, traversal: str) -> TreeNode | None:
        if not traversal:
            return None

        def read_node(pos: int) -> tuple[TreeNode, int, int]:
            # returns: value, depth, next_pos

            depth = 0

            while traversal[pos] == "-":
                depth += 1
                pos += 1

            next_pos = pos

            while next_pos < len(traversal) and traversal[next_pos].isdigit():
                next_pos += 1

            return TreeNode(int(traversal[pos:next_pos])), depth, next_pos

        pos = 0

        stack: list[TreeNode] = []

        while pos < len(traversal):
            node, depth, pos = read_node(pos)

            while stack and depth < len(stack):
                stack.pop()

            if stack:
                prev_node = stack[-1]
                if prev_node.left:
                    prev_node.right = node
                else:
                    prev_node.left = node

            stack.append(node)

        return stack[0] if stack else None
