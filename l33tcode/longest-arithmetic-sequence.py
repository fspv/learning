class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(lambda: defaultdict(lambda: 1))
        result = 0

        for pos in range(len(A)):
            for prev_pos in range(pos):
                diff = A[pos] - A[prev_pos]
                dp[pos][diff] = dp[prev_pos][diff] + 1
                result = max(result, dp[pos][diff])

        return result
