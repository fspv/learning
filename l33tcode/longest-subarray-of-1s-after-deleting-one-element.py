class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        start, end = 0, 0
        result = 0
        next_start = 0

        for pos, num in enumerate(nums):
            end = pos

            if num == 0:
                start = next_start
                next_start = pos + 1

            result = max(result, end - start)

        return result

    def longestSubarrayAdditionalMem(self, nums: List[int]) -> int:
        left_right_length = [0]

        left_right_ones = 0
        for num in nums:
            if num == 1:
                left_right_ones += 1
            else:
                left_right_ones = 0

            left_right_length.append(left_right_ones)

        result = 0
        right_left_ones = 0
        for pos in reversed(range(len(nums))):
            result = max(result, left_right_length[pos] + right_left_ones)

            if nums[pos] == 1:
                right_left_ones += 1
            else:
                right_left_ones = 0

        return result
