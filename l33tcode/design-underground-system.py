from typing import Dict
from dataclasses import dataclass


@dataclass
class RouteInfo:
    journeys: int
    avg_time: float


@dataclass
class JourneyInfo:
    start_station: str
    start_time: int


class UndergroundSystem:
    def __init__(self):
        self._station_map: Dict[str, Dict[str, RouteInfo]] = {}
        self._journeys: Dict[int, JourneyInfo] = {}

    def checkIn(self, passenger: int, station_name: str, time: int) -> None:
        self._journeys[passenger] = JourneyInfo(station_name, time)

    def checkOut(self, passenger: int, station_name: str, time: int) -> None:
        start_station = self._journeys[passenger].start_station
        start_time = self._journeys[passenger].start_time

        self._station_map.setdefault(start_station, {})
        self._station_map[start_station].setdefault(station_name, RouteInfo(0, 0))

        route_info = self._station_map[start_station][station_name]

        route_info.avg_time = (
            route_info.avg_time * route_info.journeys + (time - start_time)
        ) / (route_info.journeys + 1)
        route_info.journeys += 1

    def getAverageTime(self, start_station: str, end_station: str) -> float:
        return self._station_map[start_station][end_station].avg_time


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
