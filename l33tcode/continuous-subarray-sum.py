from typing import List
from collections import defaultdict


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mods_seen = defaultdict(lambda: False)
        prefix_sums = [0]

        for pos in range(1, len(nums) + 1):
            prefix_sums.append(prefix_sums[-1] + nums[pos - 1])
            if pos > 1:
                if k != 0:
                    mods_seen[prefix_sums[pos - 2] % k] = True
                else:
                    mods_seen[prefix_sums[pos - 2]] = True

            if k != 0 and mods_seen[prefix_sums[pos] % k]:
                return True

            if k == 0 and mods_seen[prefix_sums[pos]]:
                return True

        return False
