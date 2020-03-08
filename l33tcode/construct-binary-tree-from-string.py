# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def str2tree(self, s: str) -> TreeNode:
        def dfs(pos):
            num_start = pos

            while pos < len(s) and s[pos] not in {"(", ")"}:
                pos += 1

            new_node = TreeNode(s[num_start:pos])

            if pos < len(s) and s[pos] == "(":
                new_node.left, pos = dfs(pos + 1)

            if pos < len(s) and s[pos] == "(":
                new_node.right, pos = dfs(pos + 1)

            return new_node, pos + 1

        return dfs(0)[0] if s else None
