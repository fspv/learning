from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        result: List[int] = []

        diagonals: DefaultDict[int, List[int]] = defaultdict(list)

        for row in enumerate(len(nums)):
            for col in range(len(nums[row])):
                diagonals[col + row].append(nums[row][col])

        diagonal = 0

        while diagonal in diagonals:
            result.extend(reversed(diagonals[diagonal]))
            diagonal += 1

        return result
