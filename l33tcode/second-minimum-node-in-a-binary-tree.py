# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = [root]
        last_popped = None
        minimum = root.val
        second_minimum = -1

        while len(stack):
            if stack[-1].left is not None and \
               (last_popped is None or last_popped.right is not None):
                stack.append(stack[-1].left)
            else:
                last_popped = stack.pop()

                if (second_minimum == -1 or last_popped.val < second_minimum) and \
                   last_popped.val > minimum:
                    second_minimum = last_popped.val

                if last_popped.right is not None:
                    stack.append(last_popped.right)

        return second_minimum

# TODO: add tests
