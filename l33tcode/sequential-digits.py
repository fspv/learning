from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def digits(num: int) -> int:
            count = 0
            while num > 0:
                num //= 10
                count += 1

            return count

        def dfs(low: int, high: int, length: int, num: int) -> List[int]:
            if num * 10 ** length + 10 ** length - 1 < low:
                return []

            if num * 10 ** length > high:
                return []

            if length == 0:
                return [num]

            result = []

            next_num = num % 10 + 1
            if next_num != 10:
                result.extend(dfs(low, high, length - 1, num * 10 + next_num))

            return result

        result = []

        for length in range(digits(low), digits(high) + 1):
            for num in range(1, 10):
                result.extend(dfs(low, high, length - 1, num))

        return result
