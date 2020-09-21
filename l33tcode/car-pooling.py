from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        last = 0

        for _, _, end in trips:
            last = max(last, end)

        path = [0] * (last + 1)

        for num_passengers, begin, end in trips:
            path[begin] += num_passengers
            path[end] -= num_passengers

        passengers = 0
        for num_passengers in path:
            passengers += num_passengers
            if passengers > capacity:
                return False

        return True
