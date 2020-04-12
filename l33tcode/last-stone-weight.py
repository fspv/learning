import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones_neg = list(map(lambda x: -x, stones))
        heapq.heapify(stones_neg)

        while len(stones_neg) > 1:
            largest1 = heapq.heappop(stones_neg)
            largest2 = heapq.heappop(stones_neg)

            if largest1 != largest2:
                heapq.heappush(stones_neg, -abs(largest1 - largest2))

        return list(map(lambda x: -x, stones_neg))[0] if stones_neg else 0


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.lastStoneWeight([]) == 0

    def test_case1(self):
        assert self.sol.lastStoneWeight([2, 7, 4, 1, 8, 1]) == 1

    def test_case2(self):
        assert self.sol.lastStoneWeight([1, 1]) == 0
