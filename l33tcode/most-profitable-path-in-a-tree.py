class Solution:
    def mostProfitablePath(
        self, edges: list[list[int]], bob: int, amount: list[int]
    ) -> int:
        def build_adj_list() -> list[list[int]]:
            adj_list: list[list[int]] = [[] for _ in amount]

            for src, dst in edges:
                adj_list[src].append(dst)
                adj_list[dst].append(src)

            return adj_list

        adj_list: list[list[int]] = build_adj_list()

        stack: list[int] = []
        visited: set[int] = set()

        def find_path_to_root(node: int) -> None:
            visited.add(node)
            stack.append(node)

            if node == 0:
                for path_node in stack[: len(stack) // 2]:
                    amount[path_node] = 0
                if len(stack) % 2 == 1:
                    amount[stack[len(stack) // 2]] //= 2

            for next_node in adj_list[node]:
                if next_node not in visited:
                    find_path_to_root(next_node)

            stack.pop()

        def dfs(node: int) -> int:
            visited.add(node)
            next_nodes = [n for n in adj_list[node] if n not in visited]
            return amount[node] + (max(dfs(n) for n in next_nodes) if next_nodes else 0)

        find_path_to_root(bob)

        visited = set()

        return dfs(0)
