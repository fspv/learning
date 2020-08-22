class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = []

        for pos_right in range(len(A)):
            dp.append({0: 1})
            for pos_left in range(pos_right):
                diff = A[pos_left] - A[pos_right]
                dp[pos_right][diff] = max(
                    dp[pos_right].get(diff, 1),
                    dp[pos_left].get(diff, 1) + 1
                )

        return max(dp[-1].values())
