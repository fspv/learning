# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
            return

        head = UndirectedGraphNode(node.label)
        stack = [node]
        copy_map = {node: head}

        while len(stack):
            cur_node = stack.pop()
            cur_node_copy = copy_map[cur_node]

            for neigh in cur_node.neighbors:
                if neigh not in copy_map:
                    neigh_copy = UndirectedGraphNode(neigh.label)

                    copy_map[neigh] = neigh_copy

                    stack.append(neigh)

                cur_node_copy.neighbors.append(copy_map[neigh])

        return copy_map[node]
