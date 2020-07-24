class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        visited = set()
        path = []

        def dfs(node):
            if node in visited:
                return

            if node == len(graph) - 1:
                result.append(path + [node])
                return

            visited.add(node)

            for next_node in graph[node]:
                path.append(node)
                dfs(next_node)
                path.pop()

            visited.remove(node)

        dfs(0)

        return result
