from typing import List, Tuple, Dict
from collections import defaultdict
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
