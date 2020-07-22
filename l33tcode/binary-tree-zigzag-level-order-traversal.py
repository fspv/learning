# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        if root:
            queue.append(root)

        result = []
        direction = True

        while queue:
            queue, old_queue = deque(), queue

            level = []

            for node in old_queue if direction else reversed(old_queue):
                level.append(node.val)

            result.append(level)

            direction = not direction

            for node in old_queue:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
