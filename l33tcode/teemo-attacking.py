from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        poisoned = 0
        begin, end = -1, -1

        for cur_begin in timeSeries:
            cur_end = cur_begin + duration

            if cur_begin > end:
                poisoned += end - begin
                begin = cur_begin

            end = cur_end

        return poisoned + (end - begin)
