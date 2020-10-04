from typing import List, Dict, DefaultDict, Set
from collections import defaultdict


class Solution:
    def sequenceReconstruction(self, org: List[int], seqs: List[List[int]]) -> bool:
        def build_adj_list(seqs: List[List[int]]) -> DefaultDict[int, Set[int]]:
            adj_list: DefaultDict[int, Set[int]] = defaultdict(set)

            for seq in seqs:
                for pos in range(len(seq)):
                    adj_list.setdefault(seq[pos], set())
                for pos in range(1, len(seq)):
                    adj_list[seq[pos - 1]].add(seq[pos])

            return adj_list

        adj_list = build_adj_list(seqs)

        def dfs(org_pos: int, visited: Set[int]) -> bool:
            visited.remove(org[org_pos])

            if org_pos == len(org) - 1:
                return len(visited) == 0

            if org[org_pos + 1] in adj_list[org[org_pos]]:
                return dfs(org_pos + 1, visited)

            return False

        visited: Set[int] = set()

        def check_cycles(vertex: int, path: Set[int]) -> bool:
            path.add(vertex)
            for adj_vertex in adj_list[vertex]:
                if adj_vertex in path:
                    return False

                if adj_vertex in visited:
                    continue

                if not check_cycles(adj_vertex, path):
                    return False

            path.remove(vertex)
            visited.add(vertex)

            return True

        for vertex in list(adj_list.keys()):
            if not check_cycles(vertex, set()):
                return False

        if org and org[0] not in adj_list:
            return False

        return dfs(0, visited)
