from typing import DefaultDict, List
from collections import defaultdict
from enum import Enum


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def check_same_tree(left: TreeNode, right: TreeNode) -> bool:
            val = lambda n: n.val if n else None

            if not left and not right:
                return True

            if val(left.left) == val(right.left) and val(left.right) == val(
                right.right
            ):
                return check_same_tree(left.left, right.left) and check_same_tree(
                    left.right, right.right
                )

            return False

        nodes_map: DefaultDict[int, List[TreeNode]] = defaultdict(list)
        nodes_map_check: DefaultDict[int, List[bool]] = defaultdict(list)

        duplicate_trees: List[TreeNode] = []

        def dfs(node: TreeNode) -> None:
            matched = False
            for pos in range(len(nodes_map[node.val])):
                if check_same_tree(node, nodes_map[node.val][pos]):
                    if nodes_map_check[node.val][pos] and not matched:
                        duplicate_trees.append(node)

                    nodes_map_check[node.val][pos] = False
                    matched = True

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            nodes_map[node.val].append(node)
            nodes_map_check[node.val].append(not matched)

        dfs(root)

        return duplicate_trees
