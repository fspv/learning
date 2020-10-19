from typing import List, Tuple, Dict
import heapq
from functools import lru_cache


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        prefix_sums: Dict[int, int] = {0: 0}
        prefix_sum = 0
        min_len_intervals: List[Tuple[int, int]] = []
        min_so_far_start, min_so_far_end = -1, len(arr)

        result = len(arr) + 1

        for pos, num in enumerate(arr):
            min_len_intervals.append((min_so_far_start, min_so_far_end))
            prefix_sum += num

            if prefix_sum - target in prefix_sums:
                start, end = prefix_sums[prefix_sum - target], pos + 1
                min_start, min_end = min_len_intervals[start]

                result = min(result, end - start + min_end - min_start)

                if end - start < min_so_far_end - min_so_far_start:
                    min_so_far_start, min_so_far_end = start, end

            prefix_sums[prefix_sum] = pos + 1

        if result <= len(arr):
            return result

        return -1

    def minSumOfLengthsBruteForce(self, arr: List[int], target: int) -> int:
        prefix_sum = [0]

        for num in arr:
            prefix_sum.append(prefix_sum[-1] + num)

        target_sum_intervals: List[Tuple[int, int]] = []

        for start in range(len(arr)):
            for end in range(start, len(arr)):
                cur_sum = prefix_sum[end + 1] - prefix_sum[start]
                if cur_sum == target:
                    target_sum_intervals.append((start, end + 1))

        target_sum_intervals.sort()

        if len(target_sum_intervals) < 2:
            return -1

        @lru_cache(None)
        def dp(pos: int, prev_pos: int) -> int:
            if pos == len(target_sum_intervals):
                return len(arr) + 1

            start, end = target_sum_intervals[pos]
            prev_start, prev_end = target_sum_intervals[prev_pos]

            result = len(arr) + 1

            result = min(result, dp(pos + 1, prev_pos))

            if prev_pos < 0:
                result = min(result, dp(pos + 1, pos) + end - start)
            elif prev_end <= start:
                result = min(result, end - start)

            return result

        result = dp(0, -1)

        if result <= len(arr):
            return result

        return -1
