import heapq
from collections import defaultdict, deque
from typing import DefaultDict, Deque, Dict, List, Tuple


class Solution:
    def minRefuelStops(
        self, target: int, start_fuel: int, stations: List[List[int]]
    ) -> int:
        pos = 0
        refuels = 0
        fuel = start_fuel

        if fuel >= target:
            return refuels

        max_fuel: List[int] = []

        while pos < len(stations):
            while max_fuel and stations[pos][0] > fuel:
                fuel += -heapq.heappop(max_fuel)
                refuels += 1

            if stations[pos][0] > fuel:
                return -1

            while pos < len(stations) and stations[pos][0] <= fuel:
                heapq.heappush(max_fuel, -stations[pos][1])
                pos += 1

            if fuel >= target:
                return refuels

        while max_fuel and target > fuel:
            fuel += -heapq.heappop(max_fuel)
            refuels += 1

        if fuel >= target:
            return refuels

        return -1

    def minRefuelStopsDijkstra(
        self, target: int, start_fuel: int, stations: List[List[int]]
    ) -> int:
        if not stations:
            return 0 if start_fuel >= target else -1

        if start_fuel < stations[0][0]:
            return -1

        max_fuel: DefaultDict[
            Tuple[int, int], int
        ] = defaultdict(  # (pos, refuels) -> max fuel avail
            lambda: -1
        )

        queue: List[Tuple[int, int, int]] = [
            (0, 0, start_fuel - stations[0][0])
        ]  # (pos, refuels, fuel_left)

        while queue:
            refuels, pos, fuel = heapq.heappop(queue)
            pos = -pos

            coordinate = min(
                stations[pos][0] if pos < len(stations) else target, target
            )

            if coordinate >= target:
                return refuels

            next_coordinate = min(
                stations[pos + 1][0] if pos + 1 < len(stations) else target, target
            )
            needed_fuel = next_coordinate - coordinate

            if needed_fuel <= fuel:
                fuel_left = fuel - needed_fuel
                if fuel_left > max_fuel[(pos + 1, refuels)]:
                    heapq.heappush(queue, (refuels, -(pos + 1), fuel_left))
                    max_fuel[(pos + 1, refuels)] = fuel_left

            if needed_fuel <= fuel + stations[pos][1]:
                fuel_left = fuel + stations[pos][1] - needed_fuel
                if fuel_left > max_fuel[(pos + 1, refuels + 1)]:
                    heapq.heappush(
                        queue,
                        (refuels + 1, -(pos + 1), fuel_left),
                    )
                    max_fuel[(pos + 1, refuels + 1)] = fuel_left

        return -1
