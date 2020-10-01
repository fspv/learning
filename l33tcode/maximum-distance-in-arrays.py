from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        prev_min, prev_max = float("+inf"), float("-inf")

        max_diff = 0
        for array in arrays:
            cur_min, cur_max = min(array), max(array)
            max_diff = int(max(max_diff, cur_max - prev_min))
            max_diff = int(max(max_diff, prev_max - cur_min))
            prev_min, prev_max = min(prev_min, cur_min), max(prev_max, cur_max)

        return max_diff

    def maxDistanceBF(self, arrays: List[List[int]]) -> int:
        max_arrays = list(
            reversed(sorted((max(arrays[pos]), pos) for pos in range(len(arrays))))
        )
        min_arrays = list(sorted((min(arrays[pos]), pos) for pos in range(len(arrays))))

        max_diff = 0

        for max_array in range(len(arrays)):
            for min_array in range(len(arrays)):
                if max_arrays[max_array][1] != min_arrays[min_array][1]:
                    max_diff = max(
                        max_diff, max_arrays[max_array][0] - min_arrays[min_array][0]
                    )
                    break

        return max_diff
