from typing import List


class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.less = 0


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        result = []

        def dfs(node, to_insert, less):
            if node.val < to_insert.val:
                if node.right:
                    less += node.less + 1
                    return dfs(node.right, to_insert, less)
                else:
                    less += node.less + 1
                    node.right = to_insert
                    return less
            elif node.val >= to_insert.val:
                if node.left:
                    node.less += 1
                    return dfs(node.left, to_insert, less)
                else:
                    node.less += 1
                    node.left = to_insert
                    return less

        root = None

        for num in reversed(nums):
            if root:
                result.append(dfs(root, BSTNode(num), 0))
            else:
                root = BSTNode(num)
                result.append(0)

        return list(reversed(result))


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.countSmaller([5, 2, 6, 1]) == [2, 1, 1, 0]
