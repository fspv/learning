class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder:
            return

        nodes_map = {x: TreeNode(x) for x in inorder}
        inorder_map = {v: k for k, v in enumerate(inorder)}
        already_added = set([postorder[-1]])

        for pos_po in range(len(postorder) - 2, -1, -1):
            node = nodes_map[postorder[pos_po]]
            prev_node = nodes_map[postorder[pos_po + 1]]

            pos_io = inorder_map[node.val]
            prev_pos_io = inorder_map[prev_node.val]

            if prev_pos_io < pos_io:
                prev_node.right = node
            else:
                for value in inorder[pos_io + 1:prev_pos_io + 1]:
                    if value in already_added:
                        nodes_map[value].left = node
                        break

            already_added.add(node.val)

        return nodes_map[postorder[-1]]
