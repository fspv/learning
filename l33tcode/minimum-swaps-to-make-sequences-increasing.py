class Solution:
    def minSwap(self, A: List[int], B: List[int]) -> int:
        swaps_rev, swaps_same = 1, 0

        for pos in range(1, len(A)):
            if A[pos - 1] >= B[pos] or B[pos - 1] >= A[pos]:
                swaps_rev += 1
            elif A[pos - 1] >= A[pos] or B[pos - 1] >= B[pos]:
                swaps_rev, swaps_same = swaps_same + 1, swaps_rev
            else:
                swaps_same = min(swaps_rev, swaps_same)
                swaps_rev = swaps_same + 1

        return min(swaps_rev, swaps_same)
