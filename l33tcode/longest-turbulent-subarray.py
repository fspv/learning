from typing import List


class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        if not A:
            return 0

        max_turbulent_subarray = 1
        prev_turbulent_subarray = 0

        prev_prev = prev = A[0]

        for cur in A:
            if prev_prev < prev:
                if prev > cur:
                    prev_turbulent_subarray += 1
                elif prev < cur:
                    prev_turbulent_subarray = 2
                else:
                    prev_turbulent_subarray = 1
            elif prev_prev > prev:
                if prev < cur:
                    prev_turbulent_subarray += 1
                elif prev > cur:
                    prev_turbulent_subarray = 2
                else:
                    prev_turbulent_subarray = 1
            else:
                if prev < cur:
                    prev_turbulent_subarray = 2
                elif prev > cur:
                    prev_turbulent_subarray = 2
                else:
                    prev_turbulent_subarray = 1

            max_turbulent_subarray = max(
                max_turbulent_subarray, prev_turbulent_subarray
            )

            prev_prev, prev = prev, cur

        return max_turbulent_subarray
