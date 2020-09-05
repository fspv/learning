from typing import List, Iterator, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        def dfs(node: TreeNode) -> Iterator[TreeNode]:
            if not node:
                return

            yield from dfs(node.left)
            yield node
            yield from dfs(node.right)

        def next_node(iterator: Iterator[TreeNode]) -> Optional[TreeNode]:
            try:
                return next(iterator)
            except:
                return None

        left_iterator = dfs(root1)
        left_node = next_node(left_iterator)

        right_iterator = dfs(root2)
        right_node = next_node(right_iterator)

        result = []

        while left_node or right_node:
            if not right_node or (left_node and left_node.val < right_node.val):
                result.append(left_node.val)
                left_node = next_node(left_iterator)
            else:
                result.append(right_node.val)
                right_node = next_node(right_iterator)

        return result
