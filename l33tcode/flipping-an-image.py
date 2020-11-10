from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        rows, cols = len(A), len(A[0]) if A else 0

        def flip(row: List[int]) -> None:
            left, right = 0, cols - 1

            while left < right:
                row[left], row[right] = row[right], row[left]
                left += 1
                right -= 1

        def inverse(row: List[int]) -> None:
            for col in range(cols):
                row[col] = 1 - row[col]

        for row in range(rows):
            flip(A[row])
            inverse(A[row])

        return A
