from typing import List, Set, Tuple


class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees: List[int] = [0] * n
        has_edge: Set[Tuple[int, int]] = set()

        for src, dst in roads:
            degrees[src] += 1
            degrees[dst] += 1
            has_edge.add((src, dst))
            has_edge.add((dst, src))

        max_network_rank = 0

        # O(n*n) time complexity. The solution is not optimal, O(n + m) is
        # possible and quite obvious, but I'm too lazy today
        for src in range(n):
            for dst in range(n):
                if src == dst:
                    continue

                max_network_rank = max(
                    max_network_rank,
                    degrees[src] + degrees[dst] - int((src, dst) in has_edge),
                )

        return max_network_rank
