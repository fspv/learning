from typing import List, Dict, Iterator, Set, Deque, Tuple
from functools import lru_cache
from collections import deque


class Solution:
    def minJumps(self, array: List[int]) -> int:
        def gen_value_pos_map() -> Dict[int, List[int]]:
            value_pos_map: Dict[int, List[int]] = {}
            for pos, value in enumerate(array):
                value_pos_map.setdefault(value, [])
                value_pos_map[value].append(pos)

            for key in value_pos_map.keys():
                value_pos_map[key].reverse()

            return value_pos_map

        value_pos_map = gen_value_pos_map()

        def neighbors(pos: int) -> Iterator[int]:
            for neigh_pos in (value_pos_map[array[pos]] + [pos - 1, pos + 1]):
                if 0 <= neigh_pos < len(array) and neigh_pos != pos:
                    yield neigh_pos

        queue: Deque[Tuple[int, int]] = deque()
        min_jumps = [len(array)] * len(array)
        min_jumps[0] = 0

        queue.append((0, 0))

        while queue:
            jumps, pos = queue.popleft()

            for neigh_pos in neighbors(pos):
                if neigh_pos == len(array) - 1:
                    return jumps + 1

                if min_jumps[neigh_pos] > jumps + 1:
                    min_jumps[neigh_pos] = jumps + 1
                    queue.append((jumps + 1, neigh_pos))

        return min_jumps[-1]
