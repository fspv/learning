from typing import Union


class TreeNode:
    def __init__(self, x: Union[int, float]):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        def dfs(
            left: Union[int, float], right: Union[int, float], node: TreeNode, pos: int
        ) -> int:
            # Try to go left
            next_pos = pos + 1
            if next_pos >= len(preorder):
                return pos

            next_node = TreeNode(preorder[next_pos])

            if next_node.val < node.val:
                node.left = next_node
                pos = dfs(left, node.val, next_node, next_pos)

            # Try to go right
            next_pos = pos + 1
            if next_pos >= len(preorder):
                return pos
            next_node = TreeNode(preorder[next_pos])

            if left < next_node.val < right:
                node.right = next_node
                pos = dfs(node.val, right, next_node, next_pos)

            return pos

        root = TreeNode(preorder[0])

        dfs(float("-inf"), float("+inf"), root, 0)

        return root
