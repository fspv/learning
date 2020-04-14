from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
            left_ptr, right_ptr = 0, 0
            result = []

            while left_ptr < len(left) and right_ptr < len(right):
                left_begin, left_height = left[left_ptr]
                right_begin, right_height = right[right_ptr]

                if left_begin < right_begin:
                    right[right_ptr][1] = max(left_height, right_height)
                    result.append(left[left_ptr])
                    left_ptr += 1
                elif left_begin > right_begin:


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.getSkyline(
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        ) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
