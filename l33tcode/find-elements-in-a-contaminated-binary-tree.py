# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class FindElements:
    def __init__(self, root: TreeNode):
        self.root = root

        # Setting of values is not necessary

        # if not self.root:
        #     return
        # else:
        #     self.root.val = 0

        # stack = [self.root]

        # while stack:
        #     old_stack = stack
        #     stack = []

        #     for node in stack:
        #         if node.left:
        #             stack.append(node.left)
        #             node.left.val = node.val * 2 + 1
        #         if node.right:
        #             stack.append(node.right)
        #             node.right.val = node.val * 2 + 2

    def find(self, target: int) -> bool:
        def traverse_back(val):
            if val == 0:
                return self.root
            elif val % 2 == 1:
                prev = traverse_back((val - 1) / 2)

                if not prev:
                    return None

                if prev.left:
                    return prev.left
            else:
                prev = traverse_back((val - 2) / 2)

                if not prev:
                    return None

                if prev.right:
                    return prev.right

        return traverse_back(target) is not None


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
