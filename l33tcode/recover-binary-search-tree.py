from typing import Optional, Tuple, List, Dict, Union


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        out_of_order = []

        def dfs(
            node: TreeNode, max_left: TreeNode, min_right: TreeNode
        ) -> List[TreeNode]:
            min_left = node
            max_right = node

            if node.left:
                min_left, max_left = dfs(node.left, max_left, node)

            if node.right:
                min_right, max_right = dfs(node.right, node, min_right)

            if (
                node.val < max_left.val
                and node.val < min_right.val
                and max_left.val < min_right.val
            ):
                out_of_order.append(node)

            if (
                node.val > max_left.val
                and node.val > min_right.val
                and max_left.val < min_right.val
            ):
                out_of_order.append(node)

            return [min_left, max_right]

        if not root:
            return

        leftmost_node, rightmost_node = root, root

        while leftmost_node.left:
            leftmost_node = leftmost_node.left

        while rightmost_node.right:
            rightmost_node = rightmost_node.right

        leftmost_node.left = TreeNode(float("-inf"))
        rightmost_node.right = TreeNode(float("+inf"))

        dfs(root, TreeNode(float("-inf")), TreeNode(float("+inf")))

        leftmost_node.left = None
        rightmost_node.right = None

        node_left, node_right = out_of_order

        node_left.val, node_right.val = node_right.val, node_left.val

    def recoverTreeBubbleSort(self, root: TreeNode) -> None:
        def dfs(node: TreeNode) -> List[Union[TreeNode, TreeNode, bool]]:
            min_left, max_left = node, node
            min_right, max_right = node, node
            swaps_left, swaps_right = False, False

            if node.left:
                min_left, max_left, swaps_left = dfs(node.left)

            if node.right:
                min_right, max_right, swaps_right = dfs(node.right)

            swaps = False

            if node.val < max_left.val:
                node.val, max_left.val = max_left.val, node.val
                swaps = True

            if node.val > min_right.val:
                node.val, min_right.val = min_right.val, node.val
                swaps = True

            return [
                min(
                    node, min_left, min_right, max_left, max_right, key=lambda n: n.val
                ),
                max(
                    node, min_left, min_right, max_left, max_right, key=lambda n: n.val
                ),
                swaps_left or swaps_right or swaps,
            ]

        if not root:
            return

        while dfs(root)[2]:
            pass

    def recoverTreeOn(self, root: TreeNode) -> None:
        inorder: List[TreeNode] = []

        def dfs(node: TreeNode) -> None:
            if node.left:
                dfs(node.left)

            inorder.append(node)

            if node.right:
                dfs(node.right)

        if not root:
            return

        dfs(root)

        sorted_inorder = list(
            map(lambda n: n.val, sorted(inorder, key=lambda n: n.val))
        )
        for pos in range(len(inorder)):
            inorder[pos].val = sorted_inorder[pos]
