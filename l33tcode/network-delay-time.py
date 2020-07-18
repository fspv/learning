import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        class Node:
            def __init__(self, val):
                self.val = val
                self.children = []
                self.edge_weights = []


        def construct_graph(nodes, times, N):
            for src, dst, weight in times:
                nodes[src - 1].children.append(nodes[dst - 1])
                nodes[src - 1].edge_weights.append(weight)


        nodes = [Node(pos) for pos in range(N)]
        nodes_distances = [float("+inf") for _ in range(N)]

        construct_graph(nodes, times, N)

        heap = [(0, K - 1)]
        nodes_distances[K - 1] = 0

        while heap:
            distance, node_num = heapq.heappop(heap)

            node = nodes[node_num]

            for child, weight in zip(node.children, node.edge_weights):
                if distance + weight < nodes_distances[child.val]:
                    nodes_distances[child.val] = distance + weight
                    heapq.heappush(heap, (distance + weight, child.val))

        max_distance = max(nodes_distances)

        if max_distance == float("+inf"):
            return -1

        return max_distance
