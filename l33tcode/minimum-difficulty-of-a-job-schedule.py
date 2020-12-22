from typing import List


class Solution:
    def minDifficulty(self, job_difficulty: List[int], days: int) -> int:
        dp = [float("+inf")] * (len(job_difficulty) + 1)
        dp[-1] = 0

        for _ in range(days):
            dp_old = dp
            dp = [float("+inf")] * (len(job_difficulty) + 1)
            for job in reversed(range(len(job_difficulty))):
                max_difficulty = job_difficulty[job]
                for next_job in range(job, len(job_difficulty)):
                    max_difficulty = max(max_difficulty, job_difficulty[next_job])
                    dp[job] = min(dp[job], dp_old[next_job + 1] + max_difficulty,)

        if dp[0] > max(job_difficulty) * days:
            return -1

        return int(dp[0])
