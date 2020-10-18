from typing import List, Tuple
from functools import lru_cache


class Graph:
    def __init__(
        self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]
    ) -> None:
        def get_adj_list(roads: List[List[int]], cities: int) -> List[List[int]]:
            adj_list: List[List[int]] = [[] for _ in range(cities)]

            for start, end in roads:
                adj_list[start].append(end)
                adj_list[end].append(start)

            return adj_list

        def normalize_target_path(
            target_path_str: List[str], names: List[str]
        ) -> List[int]:
            name_to_index = {v: k for k, v in enumerate(names)}

            return [name_to_index.get(name, -1) for name in target_path_str]

        self.names = names
        self.adj_list = get_adj_list(roads, n)
        self.target_path = normalize_target_path(targetPath, names)
        self.targetPath = targetPath
        self.result_path = self.target_path

    @lru_cache(None)
    def find_path_with_min_edit_distance(
        self, city: int, length: int
    ) -> Tuple[List[int], int]:
        if length == len(self.target_path):
            return [], 0

        min_edit_distance = len(self.target_path) + 1
        min_edit_distance_path = []

        # for adj_city in sorted(self.adj_list[city], key=lambda c: c != self.target_path[length + 1]):
        for adj_city in self.adj_list[city] if city >= 0 else range(len(self.names)):
            path, edit_distance = self.find_path_with_min_edit_distance(
                adj_city, length + 1
            )
            edit_distance += int(
                self.targetPath[length] != self.names[adj_city]
            )

            if edit_distance < min_edit_distance:
                min_edit_distance = edit_distance
                min_edit_distance_path = [adj_city] + path.copy()

        return min_edit_distance_path, min_edit_distance


class Solution:
    def mostSimilar(
        self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]
    ) -> List[int]:
        graph = Graph(n, roads, names, targetPath)

        path, edit_distance = graph.find_path_with_min_edit_distance(-1, 0)

        return path
