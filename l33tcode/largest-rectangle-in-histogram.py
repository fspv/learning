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


def largest_rectangle(histogram: List[int]) -> int:
    histogram.append(0)
    stack: List[int] = []
    max_rectangle = 0

    for right_pos in range(len(histogram)):
        while stack and histogram[stack[-1]] > histogram[right_pos]:
            smallest_pos = stack.pop()
            left_pos = stack[-1] + 1 if stack else 0

            max_rectangle = max(
                max_rectangle, histogram[smallest_pos] * (right_pos - left_pos)
            )

        stack.append(right_pos)

    return max_rectangle


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return largest_rectangle(heights)
