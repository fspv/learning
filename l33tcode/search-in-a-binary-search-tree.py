class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        prev = None
        current = root

        while current is not None:
            if current.val < val:
                prev = current
                current = current.right
            elif current.val > val:
                prev = current
                current = current.left
            else:
                return current

        return current

# No tests here because tested by CLRS binary tree structure
