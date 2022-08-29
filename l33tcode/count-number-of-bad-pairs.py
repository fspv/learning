from typing import Counter, List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        counter: Counter[int] = Counter()
        bad = len(nums) * (len(nums) - 1) // 2

        for pos, num in enumerate(nums):
            bad -= counter[num - pos]
            counter[num - pos] += 1

        return bad

    def countBadPairsBruteForce(self, nums: List[int]) -> int:
        bad = 0

        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if right - left != nums[right] - nums[left]:
                    bad += 1

        return bad
