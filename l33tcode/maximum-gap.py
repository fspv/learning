import math
from typing import List


class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        min_nums, max_nums = min(nums), max(nums)

        bucket_size = math.ceil((max_nums - min_nums) / (len(nums) - 1))

        if bucket_size == 0:
            return 0

        buckets_min = [max_nums] * len(nums)
        buckets_max = [min_nums] * len(nums)
        buckets_empty = [True] * len(nums)

        for num in nums:
            bucket = (num - min_nums) // bucket_size
            buckets_empty[bucket] = False
            buckets_min[bucket] = min(buckets_min[bucket], num)
            buckets_max[bucket] = max(buckets_max[bucket], num)

        prev_max = min_nums
        max_gap = bucket_size

        for bucket in range(len(nums)):
            if not buckets_empty[bucket]:
                max_gap = max(max_gap, buckets_min[bucket] - prev_max)
                prev_max = buckets_max[bucket]

        return max_gap
