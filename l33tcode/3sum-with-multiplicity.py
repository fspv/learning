import math

from typing import List, Counter, Set, Tuple


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        MOD = 10 ** 9 + 7
        counts = Counter(arr)
        values = list(counts.keys())
        result = 0

        seen: Set[Tuple[int, int, int]] = set()

        def combinations(n: int, k: int) -> int:
            if k > n:
                return 0
            return int(math.factorial(n) / (math.factorial(n - k) * math.factorial(k)))

        for pos_first in range(len(values)):
            for pos_second in range(pos_first, len(values)):
                first, second = values[pos_first], values[pos_second]
                third = target - first - second

                first, second, third = tuple(sorted((first, second, third)))

                if (first, second, third) in seen:
                    continue

                seen.add((first, second, third))

                if first == second == third:
                    result += combinations(counts[first], 3)
                elif first == second:
                    result += combinations(counts[first], 2) * counts[third]
                elif first == third:
                    result += combinations(counts[first], 2) * counts[second]
                elif second == third:
                    result += combinations(counts[second], 2) * counts[first]
                else:
                    result += counts[first] * counts[second] * counts[third]

                result %= MOD

        return result
