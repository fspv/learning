# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p, q):
        if not p or not q:
            if not p and not q:
                return True
            else:
                return False

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            if len(stack_p) != len(stack_q):
                return False

            old_stack_p = stack_p
            old_stack_q = stack_q
            stack_p = []
            stack_q = []

            empty = True

            for pos in range(len(old_stack_p)):
                if (old_stack_p[pos].val if old_stack_p[pos] is not None else None) != \
                   (old_stack_q[pos].val if old_stack_q[pos] is not None else None):
                    return False

                if old_stack_p[pos] is not None:
                    empty = False

                if old_stack_p[pos]:
                    stack_p.append(old_stack_p[pos].left)
                    stack_p.append(old_stack_p[pos].right)
                else:
                    stack_p.append(None)
                    stack_p.append(None)
                if old_stack_q[pos]:
                    stack_q.append(old_stack_q[pos].left)
                    stack_q.append(old_stack_q[pos].right)
                else:
                    stack_q.append(None)
                    stack_q.append(None)

            if empty:
                break

        return True
