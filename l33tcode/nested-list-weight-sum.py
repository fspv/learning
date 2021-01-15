class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(node: List[NestedInteger], depth: int) -> int:
            result = 0

            for next_node in node:
                if next_node.isInteger():
                    result += depth * next_node.getInteger()
                else:
                    result += dfs(next_node.getList(), depth + 1)

            return result

        return dfs(nestedList, 1)
