from itertools import accumulate
from typing import List


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = list(accumulate(nums))

        def merge(left: int, split: int, right: int) -> None:
            left_subarray = prefix_sum[left:split]
            right_subarray = prefix_sum[split:right]

            left_subarray_ptr = 0
            right_subarray_ptr = 0

            sorted_ptr = left

            while left_subarray_ptr < len(left_subarray) or right_subarray_ptr < len(
                right_subarray
            ):
                if left_subarray_ptr == len(left_subarray):
                    prefix_sum[sorted_ptr] = right_subarray[right_subarray_ptr]
                    right_subarray_ptr += 1
                elif right_subarray_ptr == len(right_subarray):
                    prefix_sum[sorted_ptr] = left_subarray[left_subarray_ptr]
                    left_subarray_ptr += 1
                elif (
                    left_subarray[left_subarray_ptr]
                    > right_subarray[right_subarray_ptr]
                ):
                    prefix_sum[sorted_ptr] = right_subarray[right_subarray_ptr]
                    right_subarray_ptr += 1
                elif (
                    left_subarray[left_subarray_ptr]
                    <= right_subarray[right_subarray_ptr]
                ):
                    prefix_sum[sorted_ptr] = left_subarray[left_subarray_ptr]
                    left_subarray_ptr += 1

                sorted_ptr += 1

        def sort(left: int, right: int) -> int:
            if left == right:
                return 0

            if left + 1 == right:
                return int(lower <= prefix_sum[left] <= upper)

            count = 0

            split = left + (right - left) // 2

            count += sort(left, split)
            count += sort(split, right)

            right_subarray_ptr_lower = split
            right_subarray_ptr_upper = split

            for left_subarray_ptr in range(left, split):
                while (
                    right_subarray_ptr_lower < right
                    and prefix_sum[right_subarray_ptr_lower]
                    - prefix_sum[left_subarray_ptr]
                    < lower
                ):
                    right_subarray_ptr_lower += 1

                while (
                    right_subarray_ptr_upper < right
                    and prefix_sum[right_subarray_ptr_upper]
                    - prefix_sum[left_subarray_ptr]
                    <= upper
                ):
                    right_subarray_ptr_upper += 1

                count += max(right_subarray_ptr_upper, split) - min(
                    right_subarray_ptr_lower, right
                )

            merge(left, split, right)

            return count

        return sort(0, len(prefix_sum))

    def countRangeSumTLE(self, nums: List[int], lower: int, upper: int) -> int:
        prefix_sum = list(accumulate(nums))

        def bisect(array: List[int], target: int) -> int:
            left, right = 0, len(array)

            while left < right:
                mid = left + (right - left) // 2

                if array[mid] < target:
                    left = mid + 1
                else:
                    right = mid

            return left

        def merge(left: int, split: int, right: int) -> None:
            left_subarray = prefix_sum[left:split]
            right_subarray = prefix_sum[split:right]

            left_subarray_ptr = 0
            right_subarray_ptr = 0

            sorted_ptr = left

            while left_subarray_ptr < len(left_subarray) or right_subarray_ptr < len(
                right_subarray
            ):
                if left_subarray_ptr == len(left_subarray):
                    prefix_sum[sorted_ptr] = right_subarray[right_subarray_ptr]
                    right_subarray_ptr += 1
                elif right_subarray_ptr == len(right_subarray):
                    prefix_sum[sorted_ptr] = left_subarray[left_subarray_ptr]
                    left_subarray_ptr += 1
                elif (
                    left_subarray[left_subarray_ptr]
                    > right_subarray[right_subarray_ptr]
                ):
                    prefix_sum[sorted_ptr] = right_subarray[right_subarray_ptr]
                    right_subarray_ptr += 1
                elif (
                    left_subarray[left_subarray_ptr]
                    <= right_subarray[right_subarray_ptr]
                ):
                    prefix_sum[sorted_ptr] = left_subarray[left_subarray_ptr]
                    left_subarray_ptr += 1

                sorted_ptr += 1

        def sort(left: int, right: int) -> int:
            if left == right:
                return 0

            if left + 1 == right:
                return int(lower <= prefix_sum[left] <= upper)

            count = 0

            split = left + (right - left) // 2

            count += sort(left, split)
            count += sort(split, right)

            for left_subarray_ptr in range(left, split):
                right_subarray_ptr_lower = bisect(
                    prefix_sum[split:right], prefix_sum[left_subarray_ptr] + lower
                )
                right_subarray_ptr_upper = bisect(
                    prefix_sum[split:right],
                    prefix_sum[left_subarray_ptr] + upper + 1,
                )

                count += max(right_subarray_ptr_upper, 0) - min(
                    right_subarray_ptr_lower, right - split
                )

            merge(left, split, right)

            return count

        return sort(0, len(prefix_sum))
