import heapq
from collections import defaultdict
from itertools import chain
from typing import Counter, DefaultDict, Dict, List, Tuple


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counter1: Counter[int] = Counter()
        counter2: Counter[int] = Counter()
        counter3: Counter[int] = Counter()

        for num in nums:
            if counter1[num - 1] > 0:
                counter1[num - 1] -= 1
                counter2[num] += 1
            elif counter2[num - 1] > 0:
                counter2[num - 1] -= 1
                counter3[num] += 1
            elif counter3[num - 1] > 0:
                counter3[num - 1] -= 1
                counter3[num] += 1
            else:
                counter1[num] += 1

        return all(count == 0 for count in counter1.values()) and all(
            count == 0 for count in counter2.values()
        )

    def isPossibleBruteForce(self, nums: List[int]) -> bool:
        ptrs: List[int] = list(range(len(nums)))
        counts: List[int] = [1] * len(nums)

        for pos in range(len(nums)):
            for prev_pos in range(pos):
                if (
                    nums[pos] == nums[prev_pos] + 1
                    and ptrs[prev_pos] == prev_pos
                    and counts[prev_pos] == 1
                ):
                    ptrs[prev_pos] = pos
                    counts[pos] += counts[prev_pos]
                    break
            else:
                for prev_pos in range(pos):
                    if (
                        nums[pos] == nums[prev_pos] + 1
                        and ptrs[prev_pos] == prev_pos
                        and counts[prev_pos] == 2
                    ):
                        ptrs[prev_pos] = pos
                        counts[pos] += counts[prev_pos]
                        break
                else:
                    for prev_pos in range(pos):
                        if (
                            nums[pos] == nums[prev_pos] + 1
                            and ptrs[prev_pos] == prev_pos
                            and counts[prev_pos] > 2
                        ):
                            ptrs[prev_pos] = pos
                            counts[pos] += counts[prev_pos]
                            break

        for pos in range(len(nums)):
            if ptrs[pos] == pos and counts[pos] < 3:
                return False

        return True
