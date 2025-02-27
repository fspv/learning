from functools import lru_cache


class Solution:
    def jump(self, nums: list[int]) -> int:
        nums_pos = 0
        scan_pos = 0
        count = 0

        while nums_pos < len(nums) - 1:
            max_end = 0
            max_end_pos = 0

            while scan_pos <= nums_pos + nums[nums_pos]:
                if scan_pos >= len(nums) - 1:
                    return count + 1

                if scan_pos + nums[scan_pos] > max_end:
                    max_end = scan_pos + nums[scan_pos]
                    max_end_pos = scan_pos

                scan_pos += 1

            nums_pos = max_end_pos
            count += 1

        return count

    def jumpN2(self, nums: list[int]) -> int:
        @lru_cache(None)
        def dp(pos: int) -> int:
            if pos == len(nums) - 1:
                return 0
            min_jumps = len(nums) + 1
            for next_pos in reversed(
                range(pos + 1, min(len(nums), pos + nums[pos] + 1))
            ):
                min_jumps = min(min_jumps, dp(next_pos) + 1)

            return min_jumps

        return dp(0)
