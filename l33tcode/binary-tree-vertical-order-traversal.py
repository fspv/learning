from typing import List, Dict
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(node: TreeNode) -> Dict[int, List[int]]:
            lines: Dict[int, List[int]] = defaultdict(list)
            queue = deque()
            queue.append([node, 0])

            while queue:
                new_node, line = queue.popleft()

                lines[line].append(new_node.val)

                if new_node.left:
                    queue.append([new_node.left, line - 1])

                if new_node.right:
                    queue.append([new_node.right, line + 1])

            return lines

        if not root:
            return []

        lines = bfs(root)

        return list(map(lambda x: x[1], sorted(lines.items())))
