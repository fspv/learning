from typing import List
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        total = sum(node.val for node in tree)

        for node in tree:
            for child in node.children:
                total -= child.val

        return list(filter(lambda x: x.val == total, tree))[0]

    def findRoot1(self, tree: List['Node']) -> 'Node':
        min_value = min(node.val for node in tree)

        for node in tree:
            node.val = node.val - min_value + 1

        for node in tree:
            for child in node.children:
                child.val = - child.val

        root = list(filter(lambda x: x.val > 0, tree))[0]
        root.val += min_value - 1

        for node in tree:
            if node != root:
                node.val = - node.val + min_value - 1

        return root

