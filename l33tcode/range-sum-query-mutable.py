from typing import List, Optional


class RangeTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class NumArray:
    def __init__(self, nums: List[int]):
        def build_tree(left: int, right: int) -> RangeTreeNode:
            # left - included, right - not included

            middle = (left + right) // 2  # could overflow, but we're in python

            node = RangeTreeNode(nums[middle])

            if left != middle:
                node.left = build_tree(left, middle)
                node.right = build_tree(middle, right)

            if node.left:
                node.val += node.left.val
                node.val -= nums[middle]  # adjust, since middle is counted on
                                          # the right as well

            if node.right:
                node.val += node.right.val

            return node

        if not nums:
            return

        self._nums = nums
        self._range_tree = build_tree(0, len(self._nums))

    def update(self, i: int, val: int) -> None:
        def dfs(
            node: RangeTreeNode, left: int, right: int, diff: int, pos: int
        ) -> None:
            if left > right:
                return

            middle = (left + right) // 2

            node.val += diff
            if middle <= pos:
                if node.right:
                    dfs(node.right, middle, right, diff, pos)
            elif middle > pos:
                if node.left:
                    dfs(node.left, left, middle, diff, pos)

        dfs(self._range_tree, 0, len(self._nums), val - self._nums[i], i)

        self._nums[i] = val  # not really necessary

    def sumRange(self, i: int, j: int) -> int:
        def dfs(
            node: RangeTreeNode, left: int, right: int, pos_left: int, pos_right: int
        ) -> int:
            if pos_left <= left <= pos_right and pos_left <= right <= pos_right:
                return node.val

            if right - left == 1:
                return 0

            middle = (left + right) // 2

            result = 0

            if pos_left <= middle < pos_right:
                if node.left:
                    result += dfs(node.left, left, middle, pos_left, pos_right)
                if node.right:
                    result += dfs(node.right, middle, right, pos_left, pos_right)
            elif middle < pos_left:
                if node.right:
                    result += dfs(node.right, middle, right, pos_left, pos_right)
            else:
                if node.left:
                    result += dfs(node.left, left, middle, pos_left, pos_right)

            return result

        return dfs(self._range_tree, 0, len(self._nums), i, j + 1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
