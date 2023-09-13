from typing import List, Tuple


class Solution:
    def candy(self, ratings: List[int]) -> int:
        max_candies = [1] * len(ratings)

        cur_candies = 1
        for child in range(1, len(ratings)):
            if ratings[child - 1] < ratings[child]:
                cur_candies += 1
                max_candies[child] = max(max_candies[child], cur_candies)
            else:
                cur_candies = 1

        cur_candies = 1
        for child in reversed(range(len(ratings) - 1)):
            if ratings[child + 1] < ratings[child]:
                cur_candies += 1
                max_candies[child] = max(max_candies[child], cur_candies)
            else:
                cur_candies = 1

        return sum(max_candies)

    def candy_topological_sort(self, ratings: List[int]) -> int:
        def build_adj_list() -> Tuple[List[List[int]], List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(len(ratings))]
            indegrees = [0] * len(ratings)

            for child in range(len(ratings)):
                if child > 0 and ratings[child - 1] < ratings[child]:
                    adj_list[child].append(child - 1)
                    indegrees[child - 1] += 1
                if child < len(ratings) - 1 and ratings[child + 1] < ratings[child]:
                    adj_list[child].append(child + 1)
                    indegrees[child + 1] += 1

            return adj_list, indegrees

        adj_list, indegrees = build_adj_list()

        depths = [1] * len(ratings)

        def dfs(child: int) -> int:
            max_depth = 1
            for adj_child in adj_list[child]:
                max_depth = max(max_depth, dfs(adj_child) + 1)

            depths[child] = max_depth

            return max_depth

        for child in range(len(ratings)):
            if indegrees[child] == 0:
                dfs(child)

        return sum(depths)
