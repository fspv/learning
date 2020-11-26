from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        zeroes = 0
        longest_subsequence = 0

        left = 0

        for right in range(len(A)):
            if A[right] == 0:
                zeroes += 1

            while zeroes > K:
                if A[left] == 0:
                    zeroes -= 1
                left += 1

            right += 1

            longest_subsequence = max(longest_subsequence, right - left)

        return longest_subsequence
