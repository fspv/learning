from typing import List, Counter

MOD = 10 ** 9 + 7


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num: int) -> int:
            res = 0
            while num > 0:
                res *= 10
                res += num % 10
                num //= 10
            return res

        counter: Counter[int] = Counter()

        for num in nums:
            counter[num - rev(num)] += 1

        return sum((c - 1) * c // 2 for c in counter.values()) % MOD
