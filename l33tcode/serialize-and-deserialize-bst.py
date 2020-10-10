from typing import List, Tuple, Deque, Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x: int) -> None:
        self.val = x
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        queue: Deque[TreeNode] = deque()

        if root:
            queue.append(root)

        result: List[str] = []

        while queue:
            node = queue.popleft()
            result.append(str(node.val))

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """

        def tree_insert(
            root: Optional[TreeNode], new_node: TreeNode
        ) -> Optional[TreeNode]:
            node = root
            parent = None

            while node:
                parent = node
                if node.val < new_node.val:
                    node = node.right
                else:
                    node = node.left

            if not parent:
                root = new_node
            elif parent.val > new_node.val:
                parent.left = new_node
            else:
                parent.right = new_node

            return root

        if not data:
            return None

        root = None
        for val_str in data.split(","):
            root = tree_insert(root, TreeNode(int(val_str)))

        return root


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
