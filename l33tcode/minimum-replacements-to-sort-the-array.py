from typing import List, Tuple


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        limit = nums[-1]
        total_splits = 0

        def optimal_split(num: int, limit: int) -> Tuple[int, int]:
            if num % limit == 0:
                return (limit, num // limit - 1)
            else:
                splits = num // limit
                return (num // (splits + 1), splits)

        for num in reversed(nums):
            if num <= limit:
                limit = num
            else:
                limit, splits = optimal_split(num, limit)
                total_splits += splits

        return total_splits

    def minimumReplacementBruteForce(self, nums: List[int]) -> int:
        limit = nums[-1]
        total_splits = 0

        def optimal_split(num: int, limit: int) -> Tuple[int, int]:
            count = 0

            divisor = limit
            buffer = 0

            while num % divisor != 0:
                if divisor - (num % divisor) <= buffer:
                    num += divisor - (num % divisor)
                    buffer -= divisor - (num % divisor)
                    continue

                count += num // divisor
                num = num % divisor

                buffer += count

                divisor -= 1

            count += num // divisor

            return (divisor, count - 1)

        for num in reversed(nums):
            if num <= limit:
                limit = num
            else:
                limit, splits = optimal_split(num, limit)
                total_splits += splits

        return total_splits
