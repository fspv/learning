class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        rows, cols = n, m

        def condition(pos: int) -> bool:
            """
            Go over all rows and calculate the number of multiplication
            results less than pos

            Example:
                [
                  [0, 0, 0, 0, 0, 0],
                  [0, 1, 2, 3, 4, 5],
                  [0, 2, 4, 6, 8, 10],
                  [0, 3, 6, 9, 12, 15],
                  [0, 4, 8, 12, 16, 20],
                  [0, 5, 10, 15, 20, 25]
                ]
            Think about how to calculate number of elements less than 5,
            knowing that (row, col) = (1, col) * row
            """

            items = 0

            for row in range(rows):
                items += min(pos // (row + 1), cols)

            return items >= k

        left, right = 0, rows * cols

        while left < right:
            mid = (right - left) // 2 + left

            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
