from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        times = [dist[i] / speed[i] for i in range(len(dist))]

        times.sort()

        eliminated = 0

        for time in times:
            if time <= eliminated:
                break
            eliminated += 1

        return eliminated
