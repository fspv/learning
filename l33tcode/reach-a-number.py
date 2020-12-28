import math
from collections import deque
from typing import Deque, Tuple, Set


class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        steps = 0

        while target > 0:
            steps += 1
            target -= steps

        if target % 2 != 0:
            steps += 1 if steps % 2 == 0 else 2

        return steps

    def reachNumberBFS(self, target: int) -> int:
        left_limit, right_limit = - 10 ** 9 - 1, 10 ** 9 + 1
        if target == 0:
            return 0

        queue: Deque[Tuple[int, int]] = deque()

        queue.append((0, 0))

        while queue:
            steps, pos = queue.popleft()

            for jump in sorted(
                [steps + 1, -steps - 1], key=lambda j: abs(target - (pos + j))
            ):
                if pos + jump == target:
                    return steps + 1

                queue.append((steps + 1, pos + jump))

        return -1
