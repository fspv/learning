class Solution:
    def poorPigs(self, buckets: int, minutes_to_die: int, minutes_to_test: int) -> int:
        pigs = 0
        can_find = 1

        while can_find < buckets:
            can_find *= (minutes_to_test // minutes_to_die + 1)
            pigs += 1

        return pigs
