class Solution:
    def maxProfit(self, prices):
        result = 0
        min_so_far = float("+inf")

        for price in prices:
            result = max(result, price - min_so_far)
            min_so_far = min(min_so_far, price)

        return result
