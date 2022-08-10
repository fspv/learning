import math
from typing import List


class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        """
        Solution using simplified gradient descend
        """

        error = 1 / 10**5

        x_positions = sorted([float(p[0]) for p in positions])
        y_positions = sorted([float(p[1]) for p in positions])

        def distance(x_diff: float, y_diff: float) -> float:
            """
            Calculates Euclidean distance given dx and dy
            """
            return math.sqrt(x_diff**2 + y_diff**2)

        # Pick an arbitrary init point
        x_init, y_init = (
            x_positions[len(x_positions) // 2],
            y_positions[len(y_positions) // 2],
        )
        min_distance = sum(distance(x - x_init, y - y_init) for x, y in positions)

        diff = 10.0  # Initial area to look around

        while diff > error:
            # Look around in 8 directions (N, S, E, W, NE, SE, NW, SW)
            for x_new, y_new in (
                (x_init - diff, y_init),
                (x_init, y_init - diff),
                (x_init + diff, y_init),
                (x_init, y_init + diff),
                (x_init + diff, y_init + diff),
                (x_init - diff, y_init + diff),
                (x_init + diff, y_init - diff),
                (x_init - diff, y_init - diff),
            ):
                new_distance = sum(distance(x - x_new, y - y_new) for x, y in positions)

                # If found a lower distance descend there
                if new_distance < min_distance:
                    min_distance = new_distance
                    x_init, y_init = x_new, y_new
                    break
            else:
                # Found only points with bigger values, reduce lookup window
                diff /= 2

        return min_distance
