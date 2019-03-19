# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distributeCoins(self, root):
        if root is None:
            return 0

        stack = [[root, root.val]]
        last_removed = TreeNode(None)
        ans = 0

        while stack:
            print(stack)
            node, node_val = stack[-1]
            if node.left and node.left != last_removed and node.right != last_removed:
                stack.append([node.left, node.left.val])
            elif node.right and node.right != last_removed:
                stack.append([node.right, node.right.val])
            else:
                last_removed, last_removed_val = stack.pop()
                if stack:
                    stack[-1][1] += last_removed_val - 1
                ans += abs(last_removed_val - 1)

        return ans
