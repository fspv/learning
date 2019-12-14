# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False

        stack = [root]

        last_removed = None

        hashmap = Counter()

        while stack:
            node = stack[-1]

            if node.right:
                if node.right == last_removed:
                    hashmap[node.val] += 1
                    last_removed = stack.pop()
                    continue

                if not node.left or node.left == last_removed:
                    stack.append(node.right)
                    continue

            if node.left:
                if node.left != last_removed:
                    stack.append(node.left)
                    continue

            hashmap[node.val] += 1
            last_removed = stack.pop()

        for val, count in hashmap.items():
            sub_val = k - val
            if sub_val == val:
                if hashmap[val] > 1:
                    return True
            else:
                if hashmap[sub_val]:
                    return True

        return False
