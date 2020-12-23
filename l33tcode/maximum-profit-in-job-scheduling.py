import heapq
from typing import List, Tuple
from functools import lru_cache


class Solution:
    def jobScheduling(
        self, start_times: List[int], end_times: List[int], profits: List[int]
    ) -> int:
        assert len(start_times) == len(end_times)

        dp_left: List[Tuple[int, int]] = []  # [(-profit, job)]
        dp_right: List[Tuple[int, int, int]] = []  # [(end_time, profit, job)]
        max_profit = 0

        for job in sorted(range(len(profits)), key=lambda job: start_times[job]):
            while dp_right and dp_right[0][0] <= start_times[job]:
                _, tmp_profit, tmp_job = heapq.heappop(dp_right)
                heapq.heappush(dp_left, (-tmp_profit, tmp_job))

            profit = profits[job] + (-dp_left[0][0] if dp_left else 0)
            max_profit = max(max_profit, profit)

            heapq.heappush(dp_right, (end_times[job], profit, job))

        return max_profit

    def jobSchedulingBottomUpN2(
        self, start_times: List[int], end_times: List[int], profits: List[int]
    ) -> int:
        assert len(start_times) == len(end_times)

        jobs_by_start = list(
            sorted(range(len(profits)), key=lambda job: start_times[job])
        )
        jobs_by_end = list(sorted(range(len(profits)), key=lambda job: end_times[job]))

        dp = [0] * len(start_times)

        for job in jobs_by_start:
            dp[job] = profits[job]
            for prev_job in jobs_by_end:
                if start_times[job] >= end_times[prev_job]:
                    dp[job] = max(dp[job], dp[prev_job] + profits[job])
                else:
                    break

        return max(dp)

    def jobSchedulingTopDown(
        self, start_times: List[int], end_times: List[int], profits: List[int]
    ) -> int:
        assert len(start_times) == len(end_times)

        start_times.append(0)
        end_times.append(0)
        profits.append(0)

        jobs = list(zip(start_times, end_times, profits))
        jobs.sort()

        @lru_cache(None)
        def dp(job: int, prev_job: int) -> int:
            if job == len(jobs):
                return 0

            start_time, end_time, profit = jobs[job]

            return max(
                dp(job + 1, prev_job),
                (dp(job + 1, job) + profit) if start_time >= jobs[prev_job][1] else 0,
            )

        return dp(1, 0)
