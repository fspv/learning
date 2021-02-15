from typing import List, Tuple


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        def k_select(array: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            left, right = 0, len(array) - 1

            selected = 0

            while selected != k:
                pivot = array[right]
                selected = left

                for pos in range(left, right + 1):
                    if array[pos] <= pivot:
                        array[selected], array[pos] = array[pos], array[selected]

                        selected += 1

                if selected > k:
                    right = selected - 2
                    selected = 0
                elif selected < k:
                    left = selected

            return array[:k]

        array = list(map(lambda x: (x[1], x[0]), enumerate(map(sum, mat))))
        k_array = k_select(array)

        return list(map(lambda x: x[1], sorted(k_array, key=lambda x: (x[0], x[1]))))
