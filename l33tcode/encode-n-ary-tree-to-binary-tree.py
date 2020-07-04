from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: "Node") -> TreeNode:
        if not root:
            return

        queue = deque()

        broot = TreeNode(root.val)
        queue.append([root, broot])

        while queue:
            nnode, bnode = queue.popleft()

            bchild_prev = TreeNode(None)  # dummy node
            for nchild in nnode.children:
                bchild = TreeNode(nchild.val)
                queue.append([nchild, bchild])

                bnode.left = bnode.left or bchild
                bchild_prev.right = bchild
                bchild_prev = bchild

        return broot

    # Decodes your binary tree to an n-ary tree.
    def decode(self, data: TreeNode) -> "Node":
        if not data:
            return

        queue = deque()

        nroot = Node(data.val, [])
        queue.append([nroot, data])

        while queue:
            nnode, bnode = queue.popleft()

            bchild = bnode.left
            while bchild:
                nchild = Node(bchild.val, [])
                nnode.children.append(nchild)
                queue.append([nchild, bchild])
                bchild = bchild.right

        return nroot


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
