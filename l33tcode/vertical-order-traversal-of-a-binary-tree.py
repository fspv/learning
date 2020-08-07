import heapq
from typing import List, Tuple
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        def dfs(
            node: TreeNode, row: int, col: int, heap: List[Tuple[int, int, int]]
        ) -> None:
            heapq.heappush(heap, (col, row, node.val))
            if node.left:
                dfs(node.left, row + 1, col - 1, heap)
            if node.right:
                dfs(node.right, row + 1, col + 1, heap)

        if not root:
            return []

        heap: List[Tuple[int, int, int]] = []

        dfs(root, 0, 0, heap)

        result: List[List[int]] = []

        col_prev = float("-inf")  # row 1 does not exist

        while heap:
            col, row, val = heapq.heappop(heap)

            if col != col_prev:
                result.append([])

            result[-1].append(val)

            col_prev = col

        return result
