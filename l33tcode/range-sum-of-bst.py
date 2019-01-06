import unittest

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorder_tree_walk_with_limits(self, root, L, R):
        if root is None:
            return 0

        result = 0

        if root.val >= L:
            result += self.inorder_tree_walk_with_limits(root.left, L, R)
        if root.val <= R:
            result += self.inorder_tree_walk_with_limits(root.right, L, R)

        if (root.val >= L and root.val <= R):
            result += root.val

        return result


    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """

        return self.inorder_tree_walk_with_limits(root, L, R)


class TestSolution(unittest.TestCase):
    def test_cases(self):
        solution = Solution()
        root = None

        self.assertEqual(solution.rangeSumBST(root, 7, 15), 0)

        solution = Solution()
        root = TreeNode(0)

        self.assertEqual(solution.rangeSumBST(root, 7, 15), 0)

        solution = Solution()
        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.right = TreeNode(18)

        self.assertEqual(solution.rangeSumBST(root, 7, 15), 32)

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        self.assertEqual(solution.rangeSumBST(root, 6, 10), 23)

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        self.assertEqual(solution.rangeSumBST(root, 6, 6), 6)

        root = TreeNode(10)
        root.left = TreeNode(5)
        root.right = TreeNode(15)
        root.left.left = TreeNode(3)
        root.left.right = TreeNode(7)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(18)
        root.left.left.left = TreeNode(1)
        root.left.right.left = TreeNode(6)

        self.assertEqual(solution.rangeSumBST(root, 66, 66), 0)

if __name__ == "__main__":
    unittest.main()
