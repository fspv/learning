from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        def greater_exists(avg: float) -> bool:
            prefix_sum = [0.0]

            for num in nums:
                prefix_sum.append(prefix_sum[-1] + float(num) - avg)


            min_prev = float("+inf")

            for pos in range(k, len(prefix_sum)):
                min_prev = min(min_prev, prefix_sum[pos - k])

                if prefix_sum[pos] - min_prev > 0:
                    return True

            return False

        precision = 1 / 100000
        left, right = float(min(nums)), float(max(nums))

        while (right - left) > precision:
            middle = left + (right - left) / 2

            if greater_exists(middle):
                left = middle
            else:
                right = middle

        return left

    def findMaxAverageBruteForce2(self, nums: List[int], k: int) -> float:
        partial_sums: List[int] = [0]

        for num in nums:
            partial_sums.append(partial_sums[-1] + num)

        stack: List[int] = []

        max_avg = float("-inf")
        for pos in range(len(partial_sums)):
            while stack and partial_sums[stack[-1]] > partial_sums[pos]:
                first = stack.pop()
                last = pos
                if last - first >= k:
                    avg = (partial_sums[last] - partial_sums[first]) / (last - first)
                    max_avg = max(max_avg, avg)

            for first in stack:
                last = pos
                if last - first >= k:
                    avg = (partial_sums[last] - partial_sums[first]) / (last - first)
                    max_avg = max(max_avg, avg)

            stack.append(pos)

        return max_avg

    def findMaxAverageBruteForce(self, nums: List[int], k: int) -> float:
        # Just an idea, haven't tested it
        max_avg = 0.0

        for left in range(len(nums)):
            avg = 0.0
            for right in range(left, len(nums)):
                avg = avg * (right - left) / (right - left + 1) + nums[right] / (
                    right - left + 1
                )

                if right - left > k:
                    max_avg = max(max_avg, avg)

        return max_avg
