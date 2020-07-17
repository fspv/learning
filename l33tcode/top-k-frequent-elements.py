import random
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = list(map(lambda x: (x[1], x[0]), Counter(nums).items()))

        def quicksort_up_to_k(left, right):
            if left >= right:
                return

            pivot = random.randint(left, right)
            arr[pivot], arr[right] = arr[right], arr[pivot]

            sorted_ptr = left
            for pos in range(left, right + 1):
                if arr[pos] >= arr[right]:
                    arr[sorted_ptr], arr[pos] = arr[pos], arr[sorted_ptr]
                    sorted_ptr += 1

            if sorted_ptr == k:
                return
            elif sorted_ptr < k:
                quicksort_up_to_k(sorted_ptr, right)
            elif sorted_ptr > k:
                quicksort_up_to_k(left, sorted_ptr - 1)

        quicksort_up_to_k(0, len(arr) - 1)

        return [arr[pos][1] for pos in range(k)]

    def topKFrequentStraightforward(self, nums: List[int], k: int) -> List[int]:
        return list(
            map(
                lambda x: x[0],
                sorted(((k, v) for k, v in Counter(nums).items()), key=lambda x: x[1]),
            )
        )[-k:]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]

    def test_case2(self):
        assert self.sol.topKFrequent([3, 0, 1, 0], 1) == [0]

    def test_case3(self):
        assert self.sol.topKFrequent([5, 3, 1, 1, 1, 3, 5, 73, 1], 3) == [1, 5, 3]
