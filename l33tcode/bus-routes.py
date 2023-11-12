from collections import deque
from typing import Dict, List, Set, Tuple


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        bus_to_stops: Dict[int, Set[int]] = {
            bus: set(route) for bus, route in enumerate(routes)
        }
        stop_to_buses: Dict[int, Set[int]] = {}

        # Build graph
        for bus, route in enumerate(routes):
            for stop in route:
                stop_to_buses.setdefault(stop, {})
                stop_to_buses[stop].setdefault(bus, set())
                stop_to_buses[stop][bus].add(bus)

        # (num buses, bus, stop)
        queue: List[Tuple[(int, int, int)]] = deque([(0, -1, source)])
        buses_seen = {-1}

        while queue:
            num_buses, bus, stop = queue.popleft()

            if stop == target:
                return num_buses

            for next_bus in stop_to_buses[stop].keys():
                if next_bus not in buses_seen:
                    for next_stop in bus_to_stops[next_bus]:
                        if next_stop == target:
                            return num_buses + 1

                        if next_stop != stop:
                            queue.append((num_buses + 1, next_bus, next_stop))
                buses_seen.add(next_bus)

        return -1
