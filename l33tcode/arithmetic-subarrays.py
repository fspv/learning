from typing import List


class Solution:
    def checkArithmeticSubarrays(
        self, nums: List[int], l: List[int], r: List[int]
    ) -> List[bool]:
        result: List[bool] = []

        def is_arithmetic(left: int, right: int) -> bool:
            arr = sorted(nums[left:right])

            if len(arr) < 2:
                return True

            diff = arr[1] - arr[0]

            for pos in range(1, len(arr)):
                if diff != arr[pos] - arr[pos - 1]:
                    return False

            return True

        for left, right in zip(l, r):
            result.append(is_arithmetic(left, right + 1))

        return result
