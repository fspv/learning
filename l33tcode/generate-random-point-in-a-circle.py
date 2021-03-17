import random
import math
from typing import List


class Solution:
    def __init__(self, radius: float, x_center: float, y_center: float):
        self._radius = radius
        self._x, self._y = x_center, y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0.0, 2 * math.pi)
        distance = math.sqrt(random.uniform(0.0, 1.0)) * self._radius

        x = self._x + distance * math.sin(angle)
        y = self._y + distance * math.cos(angle)

        return [x, y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(radius, x_center, y_center)
# param_1 = obj.randPoint()
