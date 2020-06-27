from typing import List


class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        assert len(A) == len(B)

        if not A:
            return 0

        dominos = len(A)

        counter = {A[0]: 0, B[0]: 0}
        counter_first = {A[0]: 0, B[0]: 0}
        counter_both = {A[0]: 0, B[0]: 0}

        for pos in range(dominos):
            for num in counter.keys():
                if num == A[pos] and num == B[pos]:
                    counter[num] += 1
                    counter_both[num] += 1
                    counter_first[num] += 1
                elif num == A[pos]:
                    counter[num] += 1
                    counter_first[num] += 1
                elif num == B[pos]:
                    counter[num] += 1

        result = dominos

        for num, count in counter.items():
            if count == dominos:
                result = min(
                    result,
                    dominos - counter_first[num],
                    counter_first[num] - counter_both[num],
                )

        return result if result < dominos else -1
