from typing import List


class Solution:
    def smallestRangeII(self, array: List[int], K: int) -> int:
        array.sort()

        mins_lr: List[int] = []
        maxs_lr: List[int] = []
        mins_rl: List[int] = []
        maxs_rl: List[int] = []

        for num in array:
            if not mins_lr:
                mins_lr.append(num)
                maxs_lr.append(num)
            else:
                mins_lr.append(min(mins_lr[-1], num))
                maxs_lr.append(max(maxs_lr[-1], num))

        for num in reversed(array):
            if not mins_rl:
                mins_rl.append(num)
                maxs_rl.append(num)
            else:
                mins_rl.append(min(mins_rl[-1], num))
                maxs_rl.append(max(maxs_rl[-1], num))

        mins_rl.reverse()
        maxs_rl.reverse()

        smallest_range = max(mins_rl[0], maxs_rl[0]) - min(mins_rl[0], maxs_rl[0])

        for pos in range(1, len(array)):
            points = (
                mins_lr[pos - 1] + K,
                maxs_lr[pos - 1] + K,
                mins_rl[pos] - K,
                maxs_rl[pos] - K,
            )
            smallest_range = min(smallest_range, max(points) - min(points))

        return smallest_range
