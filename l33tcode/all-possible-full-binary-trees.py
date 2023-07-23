from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Dict, List, Optional

if TYPE_CHECKING:

    @dataclass
    class TreeNode:
        val: int
        left: Optional[TreeNode]
        right: Optional[TreeNode]


class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        # FBT - Full Binary Tree
        fbts_by_size: Dict[int, List[TreeNode]] = {
            0: [],
            1: [TreeNode(0, None, None)],
        }

        for size in range(1, n):
            # size without the root node, as tree of size 1 is trivial
            # so it is not considered here
            fbts_by_size[size + 1] = []

            for left_size in range(size + 1):
                for left_fbt in fbts_by_size[left_size]:
                    for right_fbt in fbts_by_size[size - left_size]:
                        node = TreeNode(0, left_fbt, right_fbt)
                        fbts_by_size[size + 1].append(node)

        return fbts_by_size[n]
