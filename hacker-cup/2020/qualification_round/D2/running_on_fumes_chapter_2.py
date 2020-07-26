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


def read_params(lines: Iterator[str]) -> Tuple[int, int, int, int]:
    cities_str, max_fuel_str, src_str, dst_str = next(lines).split()
    return int(cities_str), int(max_fuel_str), int(src_str) - 1, int(dst_str) - 1


def read_parent_and_cost(lines: Iterator[str]) -> Tuple[int, int]:
    parent_str, cost_str = next(lines).split()
    return int(parent_str) - 1, int(cost_str)


def read_parents_and_costs(
    lines: Iterator[str], cities: int
) -> Tuple[List[int], List[int]]:
    costs: List[int] = []
    parents: List[int] = []

    for _ in range(cities):
        parent, cost = read_parent_and_cost(lines)
        parents.append(parent)
        costs.append(cost)

    return parents, costs


def parents_to_graph(parents: List[int], cities: int) -> List[Set[int]]:
    graph: List[Set[int]] = [set() for _ in range(cities)]

    for pos, parent in enumerate(parents):
        if parent != -1:
            graph[pos].add(parent)
            graph[parent].add(pos)

    return graph


def read_job(lines: Iterator[str]) -> Tuple[int, int, List[Set[int]], List[int], int, int]:
    cities, max_fuel, src, dst = read_params(lines)
    parents, costs = read_parents_and_costs(lines, cities)

    graph = parents_to_graph(parents, cities)

    return cities, max_fuel, graph, costs, src, dst


def read_jobs(
    lines: Iterator[str],
) -> Iterator[Tuple[int, int, List[Set[int]], List[int], int, int]]:
    jobs = read_number_of_jobs(lines)

    for _ in range(jobs):
        yield read_job(lines)


def print_answer(case: int, answer: int) -> None:
    print(f"Case #{case}: {answer}")


def main() -> None:
    case = 1

    for cities, max_fuel, graph, costs, src, dst in read_jobs(sys.stdin):
        answer = cheapest_path(src, dst, max_fuel, cities, graph, costs)
        print_answer(case, answer)
        case += 1


if __name__ == "__main__":
    main()
