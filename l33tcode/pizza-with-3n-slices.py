from typing import List, Dict, Set, Optional
from enum import Enum
from functools import lru_cache


class Person(Enum):
    ME = 0
    ALICE = 1
    BOB = 2


class DoublyLinkedListNode:
    def __init__(self, val: int) -> None:
        self.val = val
        self.prev = None
        self.next = None


class Solution:
    def maxSizeSlices(self, slices: List[int]) -> int:
        levels = len(slices) // 3 + 1
        result = 0
        for start, stop in ((0, len(slices) - 1), (1, len(slices))):
            dp = [[0] * levels for _ in range(len(slices) + 2)]

            for pizza_slice in reversed(range(start, stop)):
                for level in range(levels):
                    if pizza_slice + 2 < len(dp) and level < levels - 1:
                        dp[pizza_slice][level] = max(
                            dp[pizza_slice][level],
                            dp[pizza_slice + 2][level + 1] + slices[pizza_slice],
                        )

                    dp[pizza_slice][level] = max(
                        dp[pizza_slice][level],
                        dp[pizza_slice + 1][level],
                    )

            result = max(result, dp[start][0])

        return result


    def maxSizeSlicesTopDown(self, slices: List[int]) -> int:
        @lru_cache(None)
        def dfs(pizza_slice: int, max_slice: int, level: int) -> int:
            if level == len(slices) / 3:
                return 0

            if pizza_slice > max_slice:
                return 0

            return max(
                dfs(pizza_slice + 2, max_slice, level + 1) + slices[pizza_slice],
                dfs(pizza_slice + 1, max_slice, level),
            )

        return max(dfs(1, len(slices) - 1, 0), dfs(0, len(slices) - 2, 0))

    def maxSizeSlicesBruteForce(self, slices: List[int]) -> int:
        slices_nodes = [DoublyLinkedListNode(pos) for pos in range(len(slices))]

        for pizza_slice_pos in range(len(slices)):
            prev_pizza_slice_pos = (pizza_slice_pos - 1) % len(slices)
            next_pizza_slice_pos = (pizza_slice_pos + 1) % len(slices)

            pizza_slice = slices_nodes[pizza_slice_pos]
            prev_pizza_slice = slices_nodes[prev_pizza_slice_pos]
            next_pizza_slice = slices_nodes[next_pizza_slice_pos]

            prev_pizza_slice.next = pizza_slice
            pizza_slice.prev = prev_pizza_slice

            pizza_slice.next = next_pizza_slice
            next_pizza_slice.prev = pizza_slice

        def dfs(pizza_slices_left: Set[int]) -> int:
            result = 0
            for pizza_slice_pos in list(pizza_slices_left):
                pizza_slice = slices_nodes[pizza_slice_pos]

                prev_pizza_slice = pizza_slice.prev
                next_pizza_slice = pizza_slice.next

                prev_prev_pizza_slice = prev_pizza_slice.prev
                next_next_pizza_slice = next_pizza_slice.next

                prev_prev_pizza_slice.next = next_next_pizza_slice
                next_next_pizza_slice.prev = prev_prev_pizza_slice

                pizza_slices_left.remove(pizza_slice.val)
                pizza_slices_left.remove(prev_pizza_slice.val)
                pizza_slices_left.remove(next_pizza_slice.val)

                result = max(result, dfs(pizza_slices_left) + slices[pizza_slice.val])

                pizza_slices_left.add(pizza_slice.val)
                pizza_slices_left.add(prev_pizza_slice.val)
                pizza_slices_left.add(next_pizza_slice.val)

                prev_prev_pizza_slice.next = prev_pizza_slice
                next_next_pizza_slice.prev = next_pizza_slice

            return result

        return dfs(set(range(len(slices))))


class TestSolution:
    def setup(self) -> None:
        self.sol = Solution()

    def test_case1(self) -> None:
        assert self.sol.maxSizeSlices([1,2,3,4,5,6]) == 10

    def test_case2(self) -> None:
        assert self.sol.maxSizeSlices([6,3,1,2,6,2,4,3,10,4,1,4,6,5,5,3,4,7,6,5,8,7,3,8,8,1,7,1,7,8]) == 10
