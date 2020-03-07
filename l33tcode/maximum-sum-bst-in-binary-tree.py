# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxSumBST(self, root: TreeNode) -> int:
        def dfs(node):
            max_val = 0
            is_bst = True

            left_sum, right_sum, left_min, left_max, right_min, right_max = (
                0,
                0,
                float("+inf"),
                float("-inf"),
                float("+inf"),
                float("-inf"),
            )

            if node.left:
                left_min, left_max, bst, left_sum, max_so_far = dfs(node.left)
                is_bst = is_bst and bst and node.val > left_max
                max_val = max(max_val, max_so_far)

            if node.right:
                right_min, right_max, bst, right_sum, max_so_far = dfs(node.right)
                is_bst = is_bst and bst and node.val < right_min
                max_val = max(max_val, max_so_far)

            cur_sum = node.val + left_sum + right_sum

            if is_bst:
                max_val = max(max_val, cur_sum)

            return (
                min(node.val, left_min),
                max(node.val, right_max),
                is_bst,
                cur_sum,
                max_val,
            )

        return dfs(root)[4]

    def maxSumBSTSemiBruteforce(self, root: TreeNode) -> int:
        def check_bst(node, left, right, max_sum):
            total = node.val

            if node.val <= left or node.val >= right:
                return False, 0, max_sum

            if node.left:
                res, left_sum, max_subsum = check_bst(
                    node.left, left, node.val, max_sum
                )
                max_sum = max(max_sum, max_subsum)

                if res:
                    total += left_sum
                else:
                    return False, 0, max_sum

            if node.right:
                res, right_sum, max_subsum = check_bst(
                    node.right, node.val, right, max_sum
                )
                max_sum = max(max_sum, max_subsum)

                if res:
                    total += right_sum
                else:
                    return False, 0, max_sum

            return True, total, max(max_sum, total)

        def dfs(node, max_sum):
            bst, subtree_sum, bst_max_sum = check_bst(
                node, float("-inf"), float("+inf"), max_sum
            )
            if bst:
                max_sum = max(max_sum, subtree_sum, bst_max_sum)
            else:
                if node.left:
                    max_sum = max(max_sum, dfs(node.left, max_sum))
                if node.right:
                    max_sum = max(max_sum, dfs(node.right, max_sum))

            return max_sum

        return dfs(root, 0)
