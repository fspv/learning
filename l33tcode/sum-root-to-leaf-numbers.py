# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        # O(1) space solution

        def find_predecessor(node):
            path_length = 1
            predecessor = node.left

            while predecessor and predecessor.right and predecessor.right != node:
                path_length += 1
                predecessor = predecessor.right

            return path_length, predecessor

        def preorder_traversal(node):
            total = 0
            cur_sum = 0
            while node:
                path_length, predecessor = find_predecessor(node)
                if predecessor and predecessor.right:
                    # reset sum value
                    if not predecessor.left:  # means leaf node
                        total += cur_sum

                    cur_sum = cur_sum // (10 ** path_length)

                    # reset predecessor ptr and right count
                    predecessor.right = None

                    # go right or back
                    node = node.right
                elif predecessor and not predecessor.right:
                    # visit
                    cur_sum = cur_sum * 10 + node.val

                    # set link and go left
                    predecessor.right = node
                    node = node.left
                elif not predecessor:
                    # visit
                    cur_sum = cur_sum * 10 + node.val

                    if not node.right:
                        # we've reached the rightmost point
                        total += cur_sum

                    # go right or back
                    node = node.right

            return total

        return preorder_traversal(root)

    def sumNumbersONSpace(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, prev: int) -> int:
            if not node:
                return 0

            current = prev * 10 + node.val

            if not (node.left or node.right):
                return current

            total = 0
            if node.left:
                total += dfs(node.left, current)
            if node.right:
                total += dfs(node.right, current)

            return total

        return dfs(root, 0)
