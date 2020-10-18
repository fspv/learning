from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack: List[int] = []
        area = 0

        heights.append(0)

        for pos in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[pos]:
                last_pos = stack.pop()
                prev_less = stack[-1] if stack else -1
                area = max(area, (pos - (prev_less + 1)) * heights[last_pos])

            stack.append(pos)

        return area
