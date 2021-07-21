#!/bin/python3
import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def climbingLeaderboard(ranked: List[int], player: List[int]) -> List[int]:
    ranks = [1] * len(ranked)

    rank = 1

    for pos in range(1, len(ranked)):
        if ranked[pos] != ranked[pos - 1]:
            rank += 1

        ranks[pos] = rank

    def bisect(score: int) -> int:
        left, right = 0, len(ranked) - 1

        while left < right:
            middle = left + (right - left) // 2

            if ranked[middle] <= score:
                right = middle
            else:
                left = middle + 1

        return left

    result: List[int] = [0] * len(player)

    for pos in range(len(player)):
        ranked_pos = bisect(player[pos])

        if ranked[ranked_pos] <= player[pos]:
            result[pos] = ranks[ranked_pos]
        else:
            result[pos] = ranks[ranked_pos] + 1

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write("\n".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
