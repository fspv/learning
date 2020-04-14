from typing import List


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def merge(left: List[List[int]], right: List[List[int]]) -> List[List[int]]:
            left_ptr, right_ptr = 0, 0
            left_effective, right_effective = 0, 0
            result: List[List[int]] = []

            while left_ptr < len(left) and right_ptr < len(right):
                left_begin, left_height = left[left_ptr]
                right_begin, right_height = right[right_ptr]

                if left_begin < right_begin:
                    left_effective = left_height
                    next_point = left[left_ptr][0]
                    left_ptr += 1
                elif left_begin > right_begin:
                    right_effective = right_height
                    next_point = right[right_ptr][0]
                    right_ptr += 1
                else:
                    left_effective = left_height
                    right_effective = right_height
                    next_point = right[right_ptr][0]
                    left_ptr += 1
                    right_ptr += 1

                height = max(left_effective, right_effective)
                if not result or (result and result[-1][1] != height):
                    result.append([next_point, height])

            return result + left[left_ptr:] + right[right_ptr:]

        def divide(skylines: List[List[List[int]]]) -> List[List[int]]:
            if len(skylines) == 1:
                return skylines[0]

            middle = len(skylines) // 2

            left = divide(skylines[:middle])
            right = divide(skylines[middle:])

            return merge(left, right)

        skylines = []

        for left, right, height in buildings:
            skylines.append([[left, height], [right, 0]])

        return divide(skylines) if skylines else []


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.getSkyline([]) == []

    def test_case1(self):
        assert self.sol.getSkyline(
            [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
        ) == [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]]
