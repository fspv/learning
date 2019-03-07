# TODO: not an optimal solution, have to implement a better one
# optimal runs in O(n) time
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root is None:
            return True

        stack = [root]

        while stack:
            left, right = 0, len(stack) - 1
            not_none = False

            while left <= right:
                left_value = stack[left].val if stack[left] is not None else None
                right_value = stack[right].val if stack[right] is not None else None
                not_none = left_value is not None or right_value is not None if not not_none else not_none

                if left_value != right_value:
                    return False

                left, right = left + 1, right - 1

            if not not_none:
                break

            old_stack = stack
            stack = []

            for node in old_stack:
                if node is None:
                    stack.append(None)
                    stack.append(None)
                else:
                    stack.append(node.left)
                    stack.append(node.right)

        return True


s = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right= TreeNode(2)
print(s.isSymmetric(root))
