import heapq
from typing import List, Tuple


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []

        heap: List[Tuple[int, int]] = []

        def dfs(node: TreeNode, heap: List[Tuple[int, int]]):
            depth = 0
            if node.left:
                depth = max(depth, dfs(node.left, heap))
            if node.right:
                depth = max(depth, dfs(node.right, heap))

            # Can be solved via bucket sort also, which will give use O(n) time
            # instead of O(nlogn), but I'm too tired to implement it now.
            heapq.heappush(heap, (depth, node.val))

            return depth + 1

        dfs(root, heap)

        depth = None
        result = [[]]
        while heap:
            depth_cur, node = heapq.heappop(heap)
            if depth is not None and depth != depth_cur:
                result.append([])
            depth = depth_cur
            result[-1].append(node)

        return result
