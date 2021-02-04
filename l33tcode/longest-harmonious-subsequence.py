from typing import Counter, List


class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counter = Counter(nums)
        longest_harmonious_subsequence = 0

        for num in nums:
            for count in (counter[num + 1], counter[num - 1]):
                if count:
                    longest_harmonious_subsequence = max(
                        longest_harmonious_subsequence,
                        counter[num] + count,
                    )

        return longest_harmonious_subsequence
