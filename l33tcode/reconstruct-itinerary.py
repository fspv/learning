from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Dict, List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        @dataclass
        class Airport:
            name: str
            destinations: List["Airport"] = field(default_factory=list)

            def add_destination(self, dst: "Airport") -> None:
                self.destinations.append(dst)

        airports: Dict[str, Airport] = {}

        def create_airports(tickets: List[List[str]]) -> None:
            for src, dst in tickets:
                src_airport = airports.setdefault(src, Airport(src))
                dst_airport = airports.setdefault(dst, Airport(dst))
                src_airport.add_destination(dst_airport)

            for airport in airports.values():
                airport.destinations.sort(key=lambda x: x.name, reverse=True)

        create_airports(tickets)

        answer: Deque[str] = deque()

        def dfs(airport: Airport) -> None:
            while airport.destinations:
                destination = airport.destinations.pop()
                dfs(destination)

            answer.appendleft(airport.name)

        dfs(airports["JFK"])

        return list(answer)
