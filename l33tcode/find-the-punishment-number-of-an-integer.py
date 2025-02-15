from functools import lru_cache


class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0

        @lru_cache
        def check_can_be_partitioned(target_sum: int, num: int) -> bool:
            if num == target_sum:
                return True

            order, left, right = 1, num, 0

            while left:
                right += (left % 10) * order
                order *= 10
                left //= 10

                if right > target_sum:
                    break

                if check_can_be_partitioned(target_sum - right, left):
                    return True

            return False

        for num in range(1, n + 1):
            if check_can_be_partitioned(num, num * num):
                result += num * num

        return result
