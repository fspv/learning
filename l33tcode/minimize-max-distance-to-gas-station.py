from typing import List


class Solution:
    def minmaxGasDist(self, stations: List[int], K: int) -> float:
        diffs = list(
            reversed(
                sorted(
                    float(stations[pos] - stations[pos - 1])
                    for pos in range(1, len(stations))
                )
            )
        )

        left, right = 0, diffs[0]

        while right - left > 1 / 1000000:
            middle = (left + right) / 2
            remaining = K
            diffs_pos = 0
            while remaining > 0 and diffs_pos < len(diffs):
                splits = diffs[diffs_pos] / middle
                remaining -= int(splits) if int(splits) != splits else int(splits) - 1

                diffs_pos += 1

                if remaining > 0:
                    if diffs_pos == len(diffs):
                        right = middle
                elif remaining == 0:
                    if diffs_pos < len(diffs) and diffs[diffs_pos] < middle:
                        right = middle
                    elif diffs_pos == len(diffs):
                        right = middle
                    else:
                        left = middle
                else:
                    left = middle
        else:
            return (right + left) / 2


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert (
            abs(self.sol.minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 9) - 0.5)
            < 0.001
        )

    def test_case2(self):
        assert (
            abs(
                self.sol.minmaxGasDist([10, 19, 25, 27, 56, 63, 70, 87, 96, 97], 3)
                - 9.66667
            )
            < 0.001
        )

    def test_case3(self):
        assert (
            abs(self.sol.minmaxGasDist([0, 2, 16, 18, 44, 63, 80, 84, 90, 94], 9) - 6.5)
            < 0.001
        )
