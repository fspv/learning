class Solution:
    def intervalIntersection(
        self, A: List[List[int]], B: List[List[int]]
    ) -> List[List[int]]:
        ptr_a, ptr_b = 0, 0
        result = []

        def bump_left(ptr_a, ptr_b):
            if A[ptr_a] <= B[ptr_b]:
                ptr_a += 1
            else:
                ptr_b += 1

            return ptr_a, ptr_b

        def bump_right(ptr_a, ptr_b):
            if A[ptr_a] <= B[ptr_b]:
                ptr_b += 1
            else:
                ptr_a += 1

            return ptr_a, ptr_b

        while ptr_a < len(A) and ptr_b < len(B):
            if A[ptr_a] <= B[ptr_b]:
                left, right = A[ptr_a], B[ptr_b]
            else:
                left, right = B[ptr_b], A[ptr_a]

            left_start, left_end = left
            right_start, right_end = right

            if left_end >= right_start:
                if left_end >= right_end:
                    result.append([right_start, right_end])
                    ptr_a, ptr_b = bump_right(ptr_a, ptr_b)
                elif left_end < right_end:
                    result.append([right_start, left_end])
                    ptr_a, ptr_b = bump_left(ptr_a, ptr_b)
            else:
                ptr_a, ptr_b = bump_left(ptr_a, ptr_b)

        return result
