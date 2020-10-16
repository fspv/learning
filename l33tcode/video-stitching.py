from typing import List
from functools import lru_cache


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips.sort()

        @lru_cache(None)
        def dfs(clip: int, prev_clip: int) -> int:
            prev_end = clips[prev_clip][1] if prev_clip >= 0 else 0

            if prev_end >= T:
                return 0

            min_clips = len(clips) << 1

            if clip == len(clips):
                return min_clips

            start, end = clips[clip]

            if start > prev_end:
                return min_clips

            if end > prev_end:
                min_clips = min(min_clips, dfs(clip + 1, clip) + 1,)

            min_clips = min(min_clips, dfs(clip + 1, prev_clip),)

            return min_clips

        min_clips = dfs(0, -1)

        if min_clips > len(clips):
            return -1

        return min_clips
