from typing import List, Set


class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        seen: Set[int] = set()
        cur: Set[int] = set()

        for num in A:
            cur_new: Set[int] = set()
            for num_seen in cur:
                cur_new.add(num_seen | num)

            cur_new.add(num)
            cur = cur_new
            seen |= cur

        return len(seen)

    def subarrayBitwiseORsN2(self, A: List[int]) -> int:
        dp = [[0] * len(A) for _ in range(len(A))]

        seen = set()

        count = 0

        for start in reversed(range(len(A))):
            for end in range(start, len(A)):
                if start == end:
                    dp[start][end] = A[start]
                else:
                    dp[start][end] = dp[start + 1][end] | A[start]

                if dp[start][end] not in seen:
                    count += 1
                    seen.add(dp[start][end])

        return count
