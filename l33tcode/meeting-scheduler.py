from typing import List


class Solution:
    def minAvailableDuration(
        self, slots1: List[List[int]], slots2: List[List[int]], duration: int
    ) -> List[int]:
        def intersection(left, right):
            if left[1] > right[0]:
                return [right[0], min(left[1], right[1])]

        slots1.sort()
        slots2.sort()

        slots1_ptr, slots2_ptr = 0, 0

        while slots1_ptr < len(slots1) and slots2_ptr < len(slots2):
            slot1, slot2 = slots1[slots1_ptr], slots2[slots2_ptr]

            interval = intersection(*tuple(sorted([slot1, slot2])))

            if interval and (interval[1] - interval[0]) >= duration:
                return [interval[0], interval[0] + duration]

            if slot1[1] <= slot2[1]:
                slots1_ptr += 1
            else:
                slots2_ptr += 1

        return []


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.minAvailableDuration([[0, 1]], [[0, 1]], 1) == [0, 1]

    def test_case2(self):
        assert self.sol.minAvailableDuration(
            [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8
        ) == [60, 68]

    def test_case3(self):
        assert (
            self.sol.minAvailableDuration(
                [[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 12
            )
            == []
        )
