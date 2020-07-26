#!/usr/bin/env python3

import sys
import heapq
from typing import List, Iterator, Tuple, Set


def neighbours(city: int, graph: List[Set[int]]) -> Iterator[int]:
    yield from graph[city]


def cheapest_path(
    src: int,
    dst: int,
    max_fuel: int,
    cities: int,
    graph: List[Set[int]],
    costs: List[int],
) -> int:
    heap = [(0, -max_fuel, src)]  # cost, city

    cheapest = [float("+inf")] * cities
    fuel_left = [float("-inf")] * cities
    cheapest[src] = 0
    fuel_left[src] = max_fuel

    while heap:
        cost, fuel, city = heapq.heappop(heap)

        fuel = -fuel  # fix fuel, use negative to prioritise it in heap

        cheapest[city] = min(cost, cheapest[city])
        fuel_left[city] = max(fuel, fuel_left[city])

        if city == dst:
            return cost

        for neighbour in neighbours(city, graph):
            if fuel > 0:
                neigh_cost = cost
                neigh_fuel = fuel - 1

                if (
                    neigh_cost < cheapest[neighbour]
                    or neigh_fuel > fuel_left[neighbour]
                ):
                    heapq.heappush(heap, (neigh_cost, -neigh_fuel, neighbour))

            if fuel != max_fuel and costs[city] != 0:
                neigh_cost = cost + costs[city]
                neigh_fuel = max_fuel - 1

                if (
                    neigh_cost < cheapest[neighbour]
                    or neigh_fuel > fuel_left[neighbour]
                ):
                    heapq.heappush(heap, (neigh_cost, -neigh_fuel, neighbour))

    return -1


def read_number_of_jobs(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_cities_and_fuel(lines: Iterator[str]) -> Tuple[int, int]:
    cities_str, max_fuel_str = next(lines).split()
    return int(cities_str), int(max_fuel_str)


def read_cost(lines: Iterator[str]) -> int:
    return int(next(lines))


def read_costs(lines: Iterator[str], cities: int) -> List[int]:
    costs = []

    for _ in range(cities):
        costs.append(int(next(lines)))

    return costs


def read_job(lines: Iterator[str]) -> Tuple[int, int, List[int]]:
    cities, max_fuel = read_cities_and_fuel(lines)
    costs = read_costs(lines, cities)

    return cities, max_fuel, costs


def read_jobs(lines: Iterator[str]) -> Iterator[Tuple[int, int, List[int]]]:
    jobs = read_number_of_jobs(lines)

    for _ in range(jobs):
        yield read_job(lines)


def road_graph(cities: int) -> List[Set[int]]:
    graph: List[Set[int]] = [set() for _ in range(cities)]

    for pos in range(cities):
        if pos > 0:
            graph[pos].add(pos - 1)
            graph[pos - 1].add(pos)
        if pos < cities - 1:
            graph[pos].add(pos + 1)
            graph[pos + 1].add(pos)

    return graph


def print_answer(case: int, answer: int) -> None:
    print(f"Case #{case}: {answer}")


def main() -> None:
    case = 1

    for cities, max_fuel, costs in read_jobs(sys.stdin):
        graph = road_graph(cities)
        src, dst = 0, cities - 1
        answer = cheapest_path(src, dst, max_fuel, cities, graph, costs)
        print_answer(case, answer)
        case += 1


if __name__ == "__main__":
    main()
