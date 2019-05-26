class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        for pos, h in enumerate(sorted(heights)):
            if heights[pos] != h:
                result += 1

        return result
