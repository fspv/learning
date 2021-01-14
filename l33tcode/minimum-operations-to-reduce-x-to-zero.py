import bisect
from typing import List, Deque, Tuple, Set
from collections import deque
from functools import lru_cache


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        partial_sum = [0]

        for num in nums:
            partial_sum.append(partial_sum[-1] + num)

        if partial_sum[-1] < x:
            return -1

        min_operations = len(nums) * 2

        right = 0

        for left in range(len(partial_sum)):
            while (
                right < len(partial_sum)
                and partial_sum[left] + (partial_sum[-1] - partial_sum[right]) > x
            ):
                right += 1

            if (
                right < len(partial_sum)
                and partial_sum[left] + (partial_sum[-1] - partial_sum[right]) == x
            ):
                min_operations = min(len(nums) - (right - left), min_operations)

        if min_operations <= len(nums):
            return min_operations

        return -1

    def minOperationsBinarySearch(self, nums: List[int], x: int) -> int:
        partial_sum = [0]

        for num in nums:
            partial_sum.append(partial_sum[-1] + num)

        if partial_sum[-1] < x:
            return -1

        min_operations = len(nums) * 2

        for left in range(len(partial_sum)):
            right = bisect.bisect_left(
                partial_sum,
                partial_sum[left] + partial_sum[-1] - x,
                left,
                len(partial_sum) - 1,
            )
            if partial_sum[left] + (partial_sum[-1] - partial_sum[right]) == x:
                min_operations = min(len(nums) - (right - left), min_operations)

        if min_operations <= len(nums):
            return min_operations

        return -1

    def minOperationsBFS(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        if total == x:
            return len(nums)
        if total < x:
            return -1
        queue: Deque[Tuple[int, int, int, int]] = deque()

        queue.append((0, len(nums) - 1, x, 0))

        visited: Set[Tuple[int, int, int]] = set()

        while queue:
            left, right, value, operations = queue.popleft()

            for new_left, new_right, new_value in (
                (left + 1, right, value - nums[left]),
                (left, right - 1, value - nums[right]),
            ):
                if new_value == 0:
                    return operations + 1

                if new_value < 0:
                    continue

                if new_left > new_right:
                    continue

                if (new_left, new_right, new_value) not in visited:
                    visited.add((new_left, new_right, new_value))
                    queue.append((new_left, new_right, new_value, operations + 1))

        return -1

    def minOperationsDP(self, nums: List[int], x: int) -> int:
        @lru_cache(None)
        def backtrack(left: int, right: int, value: int) -> int:
            if value < 0:
                return len(nums) * 2

            if value == 0:
                return 0

            if left > right:
                return len(nums) * 2

            return min(
                backtrack(left + 1, right, value - nums[left]) + 1,
                backtrack(left, right - 1, value - nums[right]) + 1,
            )

        operations = backtrack(0, len(nums) - 1, x)

        if operations > len(nums):
            return -1

        return operations
