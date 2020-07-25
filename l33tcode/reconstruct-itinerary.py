import heapq
from collections import deque


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        class Airport:
            def __init__(self, name):
                self.name = name
                self.destinations = []

            def add_destination(self, dst):
                self.destinations.append(dst)

        airports = {}
        answer = deque()

        def create_airports(tickets):
            for src, dst in tickets:
                src_airport = airports.setdefault(src, Airport(src))
                dst_airport = airports.setdefault(dst, Airport(dst))
                src_airport.add_destination(dst_airport)

            for airport in airports.values():
                airport.destinations.sort(key=lambda x: x.name, reverse=True)

        def dfs(airport):
            while airport.destinations:
                destination = airport.destinations.pop()
                dfs(destination)

            answer.appendleft(airport.name)

        create_airports(tickets)
        dfs(airports["JFK"])

        return list(answer)

    def findItineraryBacktrack(self, tickets: List[List[str]]) -> List[str]:
        class Airport:
            def __init__(self, name):
                self.name = name
                self.destinations = []
                self.visited = []

            def add_destination(self, dst):
                self.destinations.append(dst)
                self.visited.append(False)

        airports = {}
        answer = deque()

        def create_airports(tickets):
            for src, dst in tickets:
                src_airport = airports.setdefault(src, Airport(src))
                dst_airport = airports.setdefault(dst, Airport(dst))
                src_airport.add_destination(dst_airport)

            for airport in airports.values():
                airport.destinations.sort(key=lambda x: x.name)

        def backtrack(airport, path_length):
            if path_length == len(tickets):
                return True

            for destination_pos, destination in enumerate(airport.destinations):

                if not airport.visited[destination_pos]:
                    airport.visited[destination_pos] = True
                    if backtrack(destination, path_length + 1):
                        answer.appendleft(destination.name)
                        return True
                    airport.visited[destination_pos] = False

            return False

        create_airports(tickets)
        if backtrack(airports["JFK"], 0):
            answer.appendleft("JFK")

        return list(answer)
