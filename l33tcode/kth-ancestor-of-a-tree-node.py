from typing import Dict, List


class TreeAncestor:
    def __init__(self, n: int, parent: List[int]):
        self._parent = parent
        children: List[List[int]] = [[] for _ in parent]

        self._ancestors: List[Dict[int, int]] = [{} for _ in parent]

        for node in range(1, len(parent)):
            children[parent[node]].append(node)

        def dfs(node: int, path: List[int]) -> None:
            path.append(node)

            for child in children[node]:
                dfs(child, path)

            power = 1

            while power < len(path):
                self._ancestors[node][power] = path[-power - 1]
                power <<= 1

            path.pop()

        path: List[int] = []
        dfs(0, path)

    def getKthAncestor(self, node: int, k: int) -> int:
        while k > 0:
            rightmost_set_bit = k & -k

            if rightmost_set_bit not in self._ancestors[node]:
                return -1

            node = self._ancestors[node][rightmost_set_bit]
            k -= rightmost_set_bit

        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
