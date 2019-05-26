class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        for pos in reversed(range(len(A) - 1)):
            if A[pos] > A[pos + 1]:
                replace_pos = pos + 1
                while replace_pos + 1 < len(A) and A[replace_pos + 1] < A[pos]:
                    replace_pos += 1
                A[pos], A[replace_pos] = A[replace_pos], A[pos]
                return A[:pos + 1] + sorted(A[pos + 1:])

        return A
