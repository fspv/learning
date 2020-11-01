# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: ListNode, root: TreeNode) -> bool:
        def match(tree_node: TreeNode, list_node: ListNode) -> bool:
            next_node = list_node.next
            if not next_node:
                return True

            result = False
            if tree_node.left and next_node.val == tree_node.left.val:
                result = result or match(tree_node.left, next_node)

            if tree_node.right and next_node.val == tree_node.right.val:
                result = result or match(tree_node.right, next_node)

            return result

        def dfs(node: TreeNode) -> bool:
            if node.val == head.val:
                if match(node, head):
                    return True

            if node.left:
                if dfs(node.left):
                    return True

            if node.right:
                if dfs(node.right):
                    return True

            return False

        return dfs(root)
