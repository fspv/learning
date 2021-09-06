from typing import List


class Solution:
    def slowestKey(self, release_times: List[int], keys_pressed: str) -> str:
        prev_time = 0

        max_time_key = (0, "")

        for pos in range(len(release_times)):
            duration = release_times[pos] - prev_time
            key = keys_pressed[pos]

            prev_time = release_times[pos]

            max_time_key = max(max_time_key, (duration, key))

        return max_time_key[1]
