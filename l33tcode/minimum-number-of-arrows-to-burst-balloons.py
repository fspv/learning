from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()

        pos = 0
        arrows = 0
        while pos < len(points):
            arrows += 1
            start, end = points[pos]

            while pos < len(points) and points[pos][0] <= end:
                start = points[pos][0]
                end = min(end, points[pos][1])

                pos += 1

        return arrows
