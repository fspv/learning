from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        queue = deque()
        if root:
            queue.append((root, 1))

        while queue:
            node, depth = queue.popleft()

            children = list(filter(lambda n: n, (node.left, node.right)))

            if not children:
                return depth

            for child in children:
                queue.append((child, depth + 1))

        return 0

    def minDepthDFS(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = []
        stack.append((root, 1))

        min_depth = float("+inf")

        while stack:
            node, depth = stack.pop()

            children = list(filter(lambda n: n, (node.left, node.right)))

            for child in children:
                stack.append((child, depth + 1))

            if not children:
                min_depth = min(min_depth, depth)

        return min_depth
