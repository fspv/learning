# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        def dfs(node: TreeNode, arr: List[int], arr_pos: int):
            if arr_pos == len(arr) - 1 and node.val == arr[arr_pos]:
                return not node.left and not node.right
            elif node.val == arr[arr_pos]:
                if node.left and dfs(node.left, arr, arr_pos + 1):
                    return True
                if node.right and dfs(node.right, arr, arr_pos + 1):
                    return True

            return False

        return dfs(root, arr, 0)
