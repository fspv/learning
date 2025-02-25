class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        prev_odd_subarrays = 0
        total_odd_subarrays = 0

        for pos, num in enumerate(arr):
            if num % 2 == 0:
                prev_odd_subarrays = prev_odd_subarrays
            else:
                prev_odd_subarrays = pos - prev_odd_subarrays + 1

            total_odd_subarrays += prev_odd_subarrays

        return total_odd_subarrays % (10 ** 9 + 7)

    def numOfSubarrays2(self, arr: list[int]) -> int:
        odd, even = 0, 0
        result = 0

        for num in arr:
            prev_odd, prev_even = odd, even

            if num % 2 == 0:  # even
                even = prev_even
                odd = prev_odd
                even += 1
            else:  # odd
                even = prev_odd
                odd = prev_even
                odd += 1

            result += odd

        return result % (10 ** 9 + 7)
