from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack: List[int] = []

        for pos in range(len(heights)):
            while stack and heights[stack[-1]] <= heights[pos]:
                stack.pop()

            stack.append(pos)

        return stack
