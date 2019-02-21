# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: 'List[int]') -> 'TreeNode':
        if not nums:
            return None

        stack = []

        nums_max_val = max(nums)
        root = TreeNode(nums_max_val)
        stack.append((nums, nums_max_val, root))

        while stack:
            subarray, subarray_max_val, node = stack.pop()

            subarray_max_index = subarray.index(subarray_max_val)

            subarray_left = subarray[:subarray_max_index]
            subarray_right = subarray[subarray_max_index + 1:]

            if subarray_left:
                node_left_max_val = max(subarray_left)
                node_left = TreeNode(node_left_max_val)
                node.left = node_left
                stack.append((subarray_left, node_left_max_val, node_left))

            if subarray_right:
                node_right_max_val = max(subarray_right)
                node_right = TreeNode(node_right_max_val)
                node.right = node_right
                stack.append((subarray_right, node_right_max_val, node_right))

        return root
