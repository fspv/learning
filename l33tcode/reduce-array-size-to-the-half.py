from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        rev_counts = Counter(Counter(arr).values())

        total, nums = 0, 0
        for count in reversed(range(1, len(arr) + 1)):
            for nums_count in range(rev_counts[count]):
                total += count
                nums += 1
                if total >= len(arr) // 2:
                    return nums

    def minSetSizeNlogN(self, arr: List[int]) -> int:
        counter = Counter(arr)

        total = 0

        for pos, count in enumerate(reversed(sorted(counter.values()))):
            total += count

            if total >= len(arr) // 2:
                return pos + 1


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.minSetSize([3, 3, 3, 3, 5, 5, 5, 2, 2, 7]) == 2

    def test_case2(self):
        assert self.sol.minSetSize([7, 7, 7, 7, 7, 7]) == 1

    def test_case3(self):
        assert self.sol.minSetSize([1, 9]) == 1

    def test_case4(self):
        assert self.sol.minSetSize([1000, 1000, 3, 7]) == 1

    def test_case5(self):
        assert self.sol.minSetSize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 5

    def test_case6(self):
        assert (
            self.sol.minSetSize(
                [9, 77, 63, 22, 92, 9, 14, 54, 8, 38, 18, 19, 38, 68, 58, 19]
            )
            == 5
        )
