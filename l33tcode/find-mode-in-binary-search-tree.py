class Solution:
    def inorder_walk(self, subtree_node=None):
        # Tested in CLRS
        if subtree_node is None:
            if self.root is None:
                return []
            subtree_node = self.root

        result = []

        if subtree_node.left is not None:
            result += self.inorder_walk(subtree_node.left)

        result += [subtree_node.val]

        if subtree_node.right is not None:
            result += self.inorder_walk(subtree_node.right)

        return result

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.root = root
        all_elements = self.inorder_walk(root)

        hash_map = {}

        for element in all_elements:
            if element in hash_map:
                hash_map[element] += 1
            else:
                hash_map[element] = 1

        if not len(hash_map):
            return []

        maximum_key = max(hash_map, key=lambda x: hash_map[x])

        return [k for k, v in hash_map.items() if v == hash_map[maximum_key]]

# TODO: write tests
# TODO: write solution withou extra space
