class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
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
