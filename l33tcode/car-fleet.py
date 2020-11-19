from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int],) -> int:
        prev_time = 0
        count = len(position)

        for car_pos, car_speed in reversed(sorted(zip(position, speed))):
            target_time = (target - car_pos) / float(car_speed)

            if target_time <= prev_time:
                count -= 1
            else:
                prev_time = target_time

        return count
