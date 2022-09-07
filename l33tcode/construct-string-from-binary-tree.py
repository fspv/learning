from typing import List, Optional


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: TreeNode) -> List[str]:
            result = [str(node.val)]

            if not node.left and not node.right:
                return result

            result.append("(")
            if node.left:
                result.extend(dfs(node.left))
            result.append(")")

            if node.right:
                result.append("(")
                result.extend(dfs(node.right))
                result.append(")")

            return result

        return "".join(dfs(root))
