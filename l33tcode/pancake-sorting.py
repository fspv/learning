from typing import List


class Solution:
    def pancakeSort(self, A: List[int]) -> List[int]:
        result = []

        for n in reversed(range(1, len(A))):
            max_pos = A.index(n + 1)

            result.append(max_pos + 1)
            result.append(n + 1)

            for i in range((max_pos + 1) // 2):
                A[i], A[max_pos - i] = A[max_pos - i], A[i]

            for i in range((n + 1) // 2):
                A[i], A[n - i] = A[n - i], A[i]

        return result
