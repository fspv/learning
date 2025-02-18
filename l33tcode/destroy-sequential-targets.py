from typing import Counter


class Solution:
    def destroyTargets(self, nums: list[int], space: int) -> int:
        counter = Counter([num % space for num in nums])
        max_count = max(counter.values())

        min_num = max(nums)

        for pos in range(len(nums)):
            if counter[nums[pos] % space] == max_count:
                min_num = min(min_num, nums[pos])

        return min_num
