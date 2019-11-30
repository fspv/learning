from typing import List


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        heaters = [float("-inf")] + heaters + [float("+inf")]
        heater_ptr = 1
        result = 0

        for house in houses:
            while heaters[heater_ptr] < house:
                heater_ptr += 1

            result = max(
                result,
                min(
                    heaters[heater_ptr] - house,
                    house - heaters[heater_ptr - 1]
                )
            )

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.findRadius([], []) == 0

    def test_one1(self):
        assert self.sol.findRadius([1], [1]) == 0

    def test_one2(self):
        assert self.sol.findRadius([1], [0]) == 1

    def test_one3(self):
        assert self.sol.findRadius([1], [10]) == 9

    def test_case1(self):
        assert self.sol.findRadius([1, 2, 3], [2]) == 1

    def test_case2(self):
        assert self.sol.findRadius([1, 2, 3, 4], [1, 4]) == 1

    def test_case3(self):
        assert self.sol.findRadius(
            [282475249,622650073,984943658,144108930,470211272,101027544,457850878,458777923],
            [823564440,115438165,784484492,74243042,114807987,137522503,441282327,16531729,823378840,143542612]
        ) == 161834419
