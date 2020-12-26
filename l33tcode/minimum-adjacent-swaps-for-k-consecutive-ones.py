from collections import deque
from typing import List, Deque


class Solution:
    def minMoves(self, nums: List[int], window: int) -> int:
        ones = [pos for pos in range(len(nums)) if nums[pos] == 1]
        prefix_sums = [0]

        for pos in ones:
            prefix_sums.append(prefix_sums[-1] + pos)

        min_moves = len(nums) * len(nums)

        for pos in range(len(ones) - window + 1):
            target_pos = pos + window // 2

            left_start, left_end = pos, target_pos
            right_start, right_end = target_pos + 1, pos + window

            moves = (
                ones[target_pos] * (left_end - left_start)
                - (prefix_sums[left_end] - prefix_sums[left_start])
                - ones[target_pos] * (right_end - right_start)
                + (prefix_sums[right_end] - prefix_sums[right_start])
                - (left_end - left_start + 1) * (left_end - left_start) // 2
                - (right_end - right_start + 1) * (right_end - right_start) // 2
            )

            min_moves = min(moves, min_moves)

        return min_moves
