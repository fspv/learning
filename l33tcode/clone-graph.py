# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class SolutionOldInput:
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

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        cloned_root = Node(node.val)
        stack = [node]
        seen = {cloned_root.val: cloned_root}

        while stack:
            node = stack.pop()

            for neigh_node in node.neighbors:
                if neigh_node.val not in seen:
                    stack.append(neigh_node)
                    seen[neigh_node.val] = Node(neigh_node.val)

                seen[node.val].neighbors.append(seen[neigh_node.val])

        return cloned_root
