from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self._partial_sum = [0]

        for num in nums:
            self._partial_sum.append(self._partial_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        return self._partial_sum[right + 1] - self._partial_sum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
