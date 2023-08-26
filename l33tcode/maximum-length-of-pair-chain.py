from functools import lru_cache
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        prev_end = pairs[0][0] - 1 if pairs else 0
        count = 0

        for start, end in pairs:
            if prev_end > end:
                prev_end = end
            elif prev_end < start:
                prev_end = end
                count += 1

        return count

    def findLongestChainStack(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        stack: List[int] = []
        for start, end in pairs:
            if stack:
                if stack[-1] > end:
                    stack.pop()
                    stack.append(end)
                elif stack[-1] < start:
                    stack.append(end)
            else:
                stack.append(end)

        return len(stack)

    def findLongestChainBruteForce(self, pairs: List[List[int]]) -> int:
        pairs.sort()

        @lru_cache(None)
        def dp(prev_pair: int, pair: int) -> int:
            if pair == len(pairs):
                return 0

            max_length = 0

            if prev_pair == -1 or pairs[prev_pair][1] < pairs[pair][0]:
                max_length = max(max_length, dp(pair, pair + 1) + 1)

            max_length = max(max_length, dp(prev_pair, pair + 1))

            return max_length

        return dp(-1, 0)
