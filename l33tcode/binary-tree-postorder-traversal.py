# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        if not root:
            return []

        stack = [root]
        result = [None]

        while stack:
            node = stack[-1]

            if node.left and node.left.val != result[-1] and \
               not (node.right and node.right.val == result[-1]):
                stack.append(node.left)
                continue
            elif node.right and node.right.val != result[-1]:
                stack.append(node.right)
                continue

            stack.pop()
            result.append(node.val)

        return result[1:]


x = TreeNode(1)
x.left = TreeNode(2)
x.right = TreeNode(3)
x.left.left = TreeNode(4)
x.left.right = TreeNode(5)

s = Solution()
s.postorderTraversal(x)
