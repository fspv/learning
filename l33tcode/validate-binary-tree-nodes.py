from typing import List


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        # Find possible root
        root_candidates = set(range(n))
        for node in range(n):
            root_candidates.discard(leftChild[node])
            root_candidates.discard(rightChild[node])

        if len(root_candidates) != 1:
            return False

        root = root_candidates.pop()

        # Verify no back/cross edges and all nodes used in the tree
        to_visit = set(range(n))

        def dfs(node: int) -> bool:
            to_visit.discard(node)

            for next_node in (leftChild[node], rightChild[node]):
                if next_node == -1:
                    continue

                if next_node not in to_visit or not dfs(next_node):
                    return False

            return True

        return dfs(root) and not to_visit
