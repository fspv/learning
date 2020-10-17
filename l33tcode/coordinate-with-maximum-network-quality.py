import math
from typing import List, DefaultDict, Deque, Tuple, Set, Iterator
from collections import deque, defaultdict
from functools import lru_cache


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        @lru_cache(None)
        def distance(width: int, height: int) -> float:
            return math.sqrt(width ** 2 + height ** 2)

        def neighbours(
            x: int, y: int, seen: Set[Tuple[int, int]]
        ) -> Iterator[Tuple[int, int]]:
            for neigh_x, neigh_y in (
                (x - 1, y),
                (x, y + 1),
                (x + 1, y),
                (x, y - 1),
            ):
                if (neigh_x, neigh_y) not in seen:
                    yield neigh_x, neigh_y

        def bfs(
            x0: int, y0: int, quality: int, qualities: DefaultDict[Tuple[int, int], int]
        ) -> Tuple[int, Tuple[float, float]]:
            queue: Deque[Tuple[int, int]] = deque()

            queue.append((x0, y0))
            seen: Set[Tuple[int, int]] = set()
            seen.add((x0, y0))

            max_quality = 0
            max_quality_coordinates = (float("-inf"), float("-inf"))

            while queue:
                x, y = queue.popleft()

                tower_distance = distance(abs(x - x0), abs(y - y0))

                if tower_distance > radius:
                    continue

                qualities[(x, y)] += int(quality / (1 + tower_distance))

                max_quality, max_quality_coordinates = max(
                    (max_quality, max_quality_coordinates),
                    (qualities[(x, y)], (-x, -y)),
                )

                for neigh_x, neigh_y in neighbours(x, y, seen):
                    seen.add((neigh_x, neigh_y))
                    queue.append((neigh_x, neigh_y))

            return max_quality, max_quality_coordinates

        qualities: DefaultDict[Tuple[int, int], int] = defaultdict(int)

        max_quality = 0
        max_quality_coordinates = (float("-inf"), float("-inf"))

        for x, y, quality in towers:
            cur_max_quality, cur_max_quality_coordinates = bfs(x, y, quality, qualities)

            max_quality, max_quality_coordinates = max(
                (max_quality, max_quality_coordinates),
                (cur_max_quality, cur_max_quality_coordinates),
            )

        return [int(-max_quality_coordinates[0]), int(-max_quality_coordinates[1])]

    def bestCoordinateBruteForce(
        self, towers: List[List[int]], radius: int
    ) -> List[int]:
        def distance(x1: int, x2: int, y1: int, y2: int) -> float:
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        min_x, max_x = float("+inf"), float("-inf")
        min_y, max_y = float("+inf"), float("-inf")

        for x, y, _ in towers:
            min_x = min(min_x, x - radius)
            max_x = max(max_x, x + radius)
            min_y = min(min_y, y - radius)
            max_y = max(max_y, y + radius)

        min_x, max_x, min_y, max_y = int(min_x), int(max_x), int(min_y), int(max_y)

        max_quality = 0
        max_quality_coordinates = [-1, -1]

        for x in range(min_x, max_x + 1):
            for y in range(min_y, max_y + 1):
                quality = 0
                for tower_x, tower_y, tower_quality in towers:
                    tower_distance = distance(x, tower_x, y, tower_y)

                    if tower_distance <= radius:
                        quality += int(tower_quality / (1 + tower_distance))

                if quality > max_quality:
                    max_quality = quality
                    max_quality_coordinates = [x, y]

        return max_quality_coordinates
