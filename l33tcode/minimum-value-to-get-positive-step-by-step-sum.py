class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minimum_value = float("+inf")
        total = 0

        for num in nums:
            total += num
            minimum_value = min(minimum_value, total)

        return max(1, 1 - minimum_value)
