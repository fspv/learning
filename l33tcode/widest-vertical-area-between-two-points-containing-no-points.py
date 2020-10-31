from typing import List


class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort()

        widest_area = 0

        prev_x = float("+inf")
        for x, _ in points:
            widest_area = max(widest_area, x - prev_x)
            prev_x = x

        return widest_area
