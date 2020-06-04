class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        for row in range(len(A)):
            if A[row][0] == 0:
                for col in range(len(A[row])):
                    A[row][col] = 1 if A[row][col] == 0 else 0

        num = 0
        for col in range(len(A[0])):
            ones = sum(A[row][col] for row in range(len(A)))
            num = max(ones, len(A) - ones) + num * 2

        return num
