from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited: List[bool] = [False] * len(nums)

        def follow_cycle(start_pos: int) -> int:
            length = 1

            pos = start_pos

            while (pos := nums[pos]) != start_pos:
                visited[pos] = True
                length += 1

            return length

        max_length = 0
        for pos in range(len(nums)):
            if not visited[pos]:
                max_length = max(max_length, follow_cycle(pos))

        return max_length
