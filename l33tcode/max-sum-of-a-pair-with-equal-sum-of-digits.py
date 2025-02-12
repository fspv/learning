class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        result = -1
        max_prev: dict[int, int] = {}

        for num in nums:
            sum_digits = 0
            num_copy = num
            while num_copy:
                sum_digits += num_copy % 10
                num_copy //= 10

            if prev_num := max_prev.get(sum_digits):
                result = max(result, prev_num + num)

            max_prev[sum_digits] = max(max_prev.get(sum_digits, 0), num)

        return result
