# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            levels_left, levels_right = 0, 0

            new_node = node.left
            while new_node:
                levels_left += 1
                new_node = new_node.left

            new_node = node.right
            while new_node:
                levels_right += 1
                new_node = new_node.right

            count = 1
            if levels_left > levels_right:
                count += dfs(node.left)
                count += dfs(node.right)
            else:
                count += 2 * sum(2 ** n for n in range(levels_left))

            return count

        return dfs(root)


    def countNodesN(self, root: TreeNode) -> int:
        if root is None:
            return 0

        stack = [root]
        count = 0
        while stack:
            old_stack = stack
            stack = []

            for node in old_stack:
                count += 1
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)

        return count
