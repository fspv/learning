# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root):
        stack = [(root, root.val)]

        last_removed = TreeNode(None)
        last_removed.right = TreeNode(None)

        total = 0

        while stack:
            node, node_val = stack[-1]

            if not node.left and not node.right:
                total += node_val
                total %= (10 ** 9 + 7)

            if not node.left or \
               (node.left == last_removed or last_removed.right == None):
                last_removed, last_removed_val = stack.pop()
                if node.right:
                    stack.append((node.right, node_val * 2 + node.right.val))
            else:
                stack.append((node.left, node_val * 2 + node.left.val))

        return total


sol = Solution()

root = TreeNode(1)
root.left = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.right = TreeNode(1)
root.right.left = TreeNode(0)
root.right.right = TreeNode(1)

assert sol.sumRootToLeaf(root) == 22

root = TreeNode(1)
root_tmp = root
for i in range(1000):
    root_tmp.right = TreeNode(1)
    root_tmp = root_tmp.right

assert sol.sumRootToLeaf(root) == 376846412
