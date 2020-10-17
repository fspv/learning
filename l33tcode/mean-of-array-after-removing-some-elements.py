from typing import List


class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()

        cut_arr = arr[int(len(arr) * 0.05):int(len(arr) * 0.95)]

        return sum(cut_arr) / len(cut_arr)
