class Solution:
    def deleteTreeNodes(self, nodes: int, parent: List[int], value: List[int]) -> int:
        class TreeNode:
            def __init__(self, val):
                self.parent = None
                self.children = []
                self.val = val

        node_links = [TreeNode(val) for val in value]

        root = node_links[0]

        for pos in range(1, len(parent)):
            node = node_links[pos]
            node.parent = node_links[parent[pos]]
            node_links[parent[pos]].children.append(node)

        def dfs(node):
            total_sum, total_nodes, total_evicted_nodes = node.val, 1, 0

            for child in node.children:
                subtree_sum, subtree_nodes, subtree_nodes_evicted = dfs(child)

                total_sum += subtree_sum
                total_nodes += subtree_nodes
                total_evicted_nodes += subtree_nodes_evicted

            return (
                total_sum,
                total_nodes,
                total_nodes if total_sum == 0 else total_evicted_nodes
            )

        subtree_sum, subtree_nodes, subtree_nodes_evicted = dfs(root)

        return subtree_nodes - subtree_nodes_evicted

