import math
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        combinations = set()

        def calculate_combinations(arr, start, prev, length):
            if len(prev) == length:
                combinations.add("".join(prev))
                return

            for pos in range(start, len(arr)):
                prev.append(arr[pos])
                calculate_combinations(arr, pos + 1, prev, length)
                prev.pop()

        tiles_sorted = list(sorted(tiles))

        for length in range(1, len(tiles_sorted) + 1):
            calculate_combinations(tiles_sorted, 0, [], length)

        result = 0
        for combination in combinations:
            sub_result = math.factorial(len(combination))
            for count in Counter(combination).values():
                sub_result /= math.factorial(count)

            result += int(sub_result)

        return result
