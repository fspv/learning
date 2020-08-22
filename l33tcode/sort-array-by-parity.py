from typing import List


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        sorted_pos = 0

        for cur_pos in range(len(A)):
            if A[cur_pos] & 1 == 0:
                A[sorted_pos], A[cur_pos] = A[cur_pos], A[sorted_pos]
                sorted_pos += 1

        return A
