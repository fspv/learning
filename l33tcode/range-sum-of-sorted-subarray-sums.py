class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []

        count = 0

        for pos_left in range(len(nums)):
            partial_sum = 0
            for pos_right in range(pos_left, len(nums)):
                partial_sum += nums[pos_right]
                sums.append(partial_sum)
                count += 1

        sums.sort()

        return sum(sums[left - 1:right]) % (10 ** 9 + 7)
