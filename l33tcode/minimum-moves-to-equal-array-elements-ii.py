from typing import List


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        moves = sum(nums) - min(nums) * len(nums)

        min_moves = moves

        for pos in range(1, len(nums)):
            diff = nums[pos] - nums[pos - 1]
            moves -= diff * (len(nums) - pos)
            moves += diff * pos

            min_moves = min(min_moves, moves)

        return min_moves
