from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestKValues(
        self, root: Optional[TreeNode], target: float, k: int
    ) -> List[int]:
        stack_left: List[TreeNode] = []
        stack_right: List[TreeNode] = []
        result_left: List[int] = []
        result_right: List[int] = []

        node = root

        while node:
            if node.val <= target:
                stack_left.append(node)
                node = node.right
            else:
                stack_right.append(node)
                node = node.left

        for _ in range(k):
            add_less = False
            if stack_left and stack_right:
                if target - stack_left[-1].val < stack_right[-1].val - target:
                    add_less = True
            elif stack_left:
                add_less = True
            elif stack_right:
                pass
            else:
                break

            if add_less:
                node = stack_left.pop()
                result_left.append(node.val)
                node = node.left
                if node:
                    stack_left.append(node)
                    node = node.right

                    while node:
                        stack_left.append(node)
                        node = node.right
            else:
                node = stack_right.pop()
                result_right.append(node.val)

                node = node.right

                if node:
                    stack_right.append(node)
                    node = node.left

                    while node:
                        stack_right.append(node)
                        node = node.left

        return list(reversed(result_left)) + result_right
