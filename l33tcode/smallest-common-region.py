from typing import List
from functools import lru_cache


class Region:
    def __init__(self, name):
        self.name = name
        self.children = set()
        self.parent = None


class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        region_map = {}

        for region in regions:
            node = region_map.get(region[0], Region(region[0]))
            region_map[node.name] = node

            for sub_region in region[1:]:
                sub_node = region_map.get(sub_region, Region(sub_region))
                region_map[sub_node.name] = sub_node
                node.children.add(sub_node)
                sub_node.parent = node

        @lru_cache
        def find_lca(name, source, target):
            if name == target:
                return True

            node = region_map[name]

            for sub_node in node.children:
                if find_lca(sub_node.name, source, target):
                    return True

            return False

        cur_node = region_map[region1]

        while not find_lca(cur_node.name, region1, region2):
            cur_node = cur_node.parent

        return cur_node.name
