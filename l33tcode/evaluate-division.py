from typing import List, Tuple, Dict
from collections import defaultdict, Counter
from itertools import chain


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        def find(array: Dict[str, Tuple[str, float]], pos: str):
            root = pos
            div_result = 1.0

            while root != array[root][0]:
                div_result *= array[root][1]
                root = array[root][0]

            div_result_max = div_result

            while pos != root:
                array[pos] = array[pos][0], div_result
                array[pos], pos = (root, div_result), array[pos][0]
                div_result /= array[pos][1]

            return root, div_result_max

        def union(
            root_left: str,
            root_right: str,
            array: Dict[str, Tuple[str, float]],
            count: Dict[str, int],
            div: float,
        ):
            if count[root_left] > count[root_right]:
                array[root_right] = root_left, div
                count[root_left] += count[root_right]
            else:
                array[root_left] = root_right, 1 / div
                count[root_right] += count[root_left]

        array: Dict[str, Tuple[str, float]] = {}
        count: Dict[str, int] = defaultdict(lambda: 1)

        for eq, value in zip(equations, values):
            left, right = eq
            if not left in array:
                array[left] = (left, 1)
            if not right in array:
                array[right] = (right, 1)

            root_left, div_root_left = find(array, left)
            root_right, div_root_right = find(array, right)

            if root_left != root_right:
                union(
                    root_left,
                    root_right,
                    array,
                    count,
                    div_root_left * value / div_root_right,
                )

        result = []

        for left, right in queries:
            if left not in array or right not in array:
                result.append(-1.0)
                continue

            root_left, div_root_left = find(array, left)
            root_right, div_root_right = find(array, right)

            if root_left == root_right:
                result.append(div_root_right / div_root_left)
            else:
                result.append(-1.0)

        return result


class RatioFinder:
    def __init__(self) -> None:
        self._adj_list: Dict[str, str] = {}
        self._edges_weight: Dict[Tuple[str, str], float] = {}
        self._vertex_count: defaultdict = defaultdict(lambda: 1)

    def _find(self, vertex: str) -> Tuple[float, str]:
        root = vertex
        val = 1.0
        while self._adj_list[root] != root:
            val *= self._edges_weight[(root, self._adj_list[root])]
            root = self._adj_list[root]

        tmp_val = val
        while self._adj_list[vertex] != root:
            self._edges_weight[(vertex, root)] = tmp_val
            tmp_val /= self._edges_weight[(vertex, self._adj_list[vertex])]
            self._adj_list[vertex], vertex = root, self._adj_list[vertex]

        return val, root

    def _union(
        self,
        root_left: str,
        root_right: str,
        val_left: float,
        val_right: float,
        result: float,
    ) -> None:
        if self._vertex_count[root_left] <= self._vertex_count[root_right]:
            val_less, root_less, val_more, root_more = (
                val_left,
                root_left,
                val_right,
                root_right,
            )
            self._edges_weight[(root_less, root_more)] = 1.0 / val_less * result * val_more
        else:
            val_less, root_less, val_more, root_more = (
                val_right,
                root_right,
                val_left,
                root_left,
            )
            self._edges_weight[(root_less, root_more)] = 1.0 / (1.0 / val_less * result / val_more)

        self._vertex_count[root_more] += self._vertex_count[root_less]
        self._adj_list[root_less] = self._adj_list[root_more]

    def add_equation(self, left: str, right: str, result: float) -> None:
        if left not in self._adj_list:
            self._adj_list[left] = left

        if right not in self._adj_list:
            self._adj_list[right] = right

        val_left, root_left = self._find(left)
        val_right, root_right = self._find(right)

        if root_left != root_right:
            self._union(root_left, root_right, val_left, val_right, result)

    def calculate(self, left: str, right: str) -> float:
        if left not in self._adj_list or right not in self._adj_list:
            return -1.0

        val_left, root_left = self._find(left)
        val_right, root_right = self._find(right)

        if root_left == root_right:
            return val_left / val_right
        else:
            return -1.0


class Solution2:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        ratio_finder = RatioFinder()

        for pos in range(len(equations)):
            ratio_finder.add_equation(equations[pos][0], equations[pos][1], values[pos])

        result = []

        for left, right in queries:
            result.append(ratio_finder.calculate(left, right))

        return result
