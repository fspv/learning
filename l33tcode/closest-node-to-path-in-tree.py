from typing import List, Set


class Solution:
    def closestNode(
        self, n: int, edges: List[List[int]], query: List[List[int]]
    ) -> List[int]:
        def gen_adj_list(size: int, edges: List[List[int]]) -> List[Set[int]]:
            adj_list: List[Set[int]] = [set() for _ in range(size)]

            for src, dst in edges:
                adj_list[src].add(dst)
                adj_list[dst].add(src)

            return adj_list

        def make_directed_tree(adj_list: List[Set[int]]) -> None:
            def _dfs(node: int) -> None:
                for child in adj_list[node]:
                    adj_list[child].discard(node)
                    _dfs(child)

            _dfs(0)

        adj_list: List[Set[int]] = gen_adj_list(n, edges)
        make_directed_tree(adj_list)

        def lca(first: int, second: int) -> int:
            result = -1

            def _dfs(node: int) -> int:
                nonlocal result

                count = 0

                if node == first:
                    count += 1

                if node == second:
                    count += 1

                for child in adj_list[node]:
                    if count == 2:
                        break

                    count += _dfs(child)

                    if count == 2:
                        break

                if count == 2 and result == -1:
                    result = node

                return count

            _dfs(0)

            return result

        result: List[int] = []

        for src, dst, node in query:
            lca_src_dst = lca(src, dst)
            lca_src_node = lca(src, node)
            lca_dst_node = lca(dst, node)

            """
            sd-sn sd-dn sn-dn
             =      =     =   root
             =      =    !=   invalid
             =     !=    !=   dn
             !=    !=    !=   invalid
             !=    !=     =   sn or dn
             !=     =     =   invalid
             !=     =    !=   sn
              =    !=     =   invalid
            """

            if lca_src_dst == lca_src_node == lca_dst_node:
                result.append(lca_src_dst)
            elif (
                lca_src_dst != lca_src_node
                and lca_src_dst == lca_dst_node
                and lca_src_node != lca_dst_node
            ):
                result.append(lca_src_node)
            elif (
                lca_src_dst != lca_dst_node
                and lca_src_dst == lca_src_node
                and lca_src_node != lca_dst_node
            ):
                result.append(lca_dst_node)
            elif (
                lca_src_dst != lca_src_node
                and lca_src_dst != lca_dst_node
                and lca_src_node == lca_dst_node
            ):
                result.append(lca_src_dst)

        return result
