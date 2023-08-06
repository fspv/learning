import math
from functools import cache


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        if k > n:
            return 0

        @cache
        def dp(songs: int) -> int:
            count = 1

            for song in range(goal):
                count *= songs - min(song, k)

            for song in range(songs):
                count -= math.comb(songs, song) * dp(song)

            return count

        return dp(n) % (10 ** 9 + 7)
