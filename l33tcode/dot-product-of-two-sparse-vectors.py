from typing import List, Tuple


class SparseVector:
    def __init__(self, nums: List[int]):
        self.vector: List[Tuple[int, int]] = []

        for pos, num in enumerate(nums):
            if num != 0:
                self.vector.append((num, pos))

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        left, right = self.vector, vec.vector
        left_ptr, right_ptr = 0, 0

        product = 0

        while left_ptr < len(left) and right_ptr < len(right):
            left_num, left_pos = left[left_ptr]
            right_num, right_pos = right[right_ptr]

            if left_pos == right_pos:
                product += left_num * right_num
                left_ptr += 1
                right_ptr += 1
            elif left_pos < right_pos:
                left_ptr += 1
            else:
                right_ptr += 1

        return product


# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
