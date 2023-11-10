from collections import defaultdict
from typing import Counter, DefaultDict, List, Set


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        # Build graph
        graph: DefaultDict[int, Set[int]] = defaultdict(set)
        indegrees: Counter[int] = Counter()
        for src, dst in adjacentPairs:
            graph[src].add(dst)
            graph[dst].add(src)
            indegrees[src] += 1
            indegrees[dst] += 1

        # Find one of the two edge nodes
        edge_node = 0
        for node, indegree in indegrees.items():
            if indegree == 1:
                edge_node = node
                break

        # Traverse from the edge
        prev_node = edge_node
        node = graph[prev_node].pop()

        result: List[int] = [edge_node]

        while indegrees[node] != 1:
            result.append(node)
            graph[node].discard(prev_node)
            prev_node = node
            node = graph[prev_node].pop()

        # Append the second edge node
        result.append(node)

        return result
