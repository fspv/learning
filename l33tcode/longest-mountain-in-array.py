from typing import List
from enum import Enum


class Direction(Enum):
    UP = 0
    DOWN = 1
    STRAIGHT = 2


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0

        prev_direction = Direction.DOWN
        start = -1

        longest_mountain = 0

        for pos in range(len(A) - 1):
            if A[pos] < A[pos + 1]:
                if prev_direction == Direction.DOWN:
                    start = pos
                elif prev_direction == Direction.STRAIGHT:
                    start = pos

                prev_direction = Direction.UP
            elif A[pos] > A[pos + 1]:
                prev_direction = Direction.DOWN
                if start != -1:
                    longest_mountain = max(longest_mountain, pos - start + 2)
            else:
                start = -1
                prev_direction = Direction.STRAIGHT

        return longest_mountain
