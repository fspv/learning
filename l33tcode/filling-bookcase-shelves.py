from typing import List
from functools import lru_cache


class Solution:
    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        dp = [float("+inf")] * (len(books) + 1)
        dp[0] = 0

        for start in range(len(books)):
            level_width = 0
            level_height = 0

            end = start
            while level_width <= shelf_width and end <= len(books):
                dp[end] = min(dp[end], dp[start] + level_height,)
                if end < len(books):
                    width, height = books[end]
                    level_width += width
                    level_height = max(level_height, height)
                end += 1

        return dp[-1]

    def minHeightShelvesTopDown(self, books: List[List[int]], shelf_width: int) -> int:
        @lru_cache(None)
        def dp(book: int, level_height: int, level_width: int) -> int:
            if book == len(books):
                return level_height

            width, height = books[book]

            total_height = float("+inf")

            if level_width + width < shelf_width:
                total_height = min(
                    dp(book + 1, max(level_height, height), level_width + width),
                    dp(book + 1, 0, 0) + max(level_height, height),
                    total_height,
                )
            elif level_width + width == shelf_width:
                total_height = min(
                    dp(book + 1, 0, 0) + max(level_height, height), total_height,
                )
            elif level_width + width > shelf_width:
                total_height = min(dp(book, 0, 0) + level_height, total_height,)

            return total_height

        return dp(0, 0, 0)
