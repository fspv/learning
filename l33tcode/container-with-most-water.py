class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0, len(heights) - 1
        result = 0

        while left < right:
            result = max(result, (right - left) * min(heights[left], heights[right]))

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return result
