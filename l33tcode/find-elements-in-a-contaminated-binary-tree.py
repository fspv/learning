from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass


if TYPE_CHECKING:

    @dataclass
    class TreeNode:
        val: int
        left: TreeNode | None = None
        right: TreeNode | None = None


class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root

    def find(self, target: int) -> bool:
        def traverse_back(val: float) -> TreeNode | None:
            if val == 0:
                return self.root
            elif val % 2 == 1:
                prev = traverse_back((val - 1) / 2)

                if not prev:
                    return None

                if prev.left:
                    return prev.left
            else:
                prev = traverse_back((val - 2) / 2)

                if not prev:
                    return None

                if prev.right:
                    return prev.right

        return traverse_back(target) is not None
