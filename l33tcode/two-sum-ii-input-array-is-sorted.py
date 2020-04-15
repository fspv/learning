from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        def find(left: int, right: int, numbers: List[int], target: int) -> int:
            while left < right - 1:
                middle = (left + right) // 2
                if numbers[middle] < target:
                    left = middle
                elif numbers[middle] > target:
                    right = middle
                else:
                    return middle

            return middle

        left, right = 0, len(numbers) - 1

        while (num_sum := numbers[left] + numbers[right]) != target:
            if num_sum > target:
                right = find(left, right, numbers, target - numbers[left])
            elif num_sum < target:
                left = find(left, right, numbers, target - numbers[right])

        return [left + 1, right + 1]


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.twoSum([2, 7, 11, 15], 9) == [1, 2]

    def test_case2(self):
        assert self.sol.twoSum([2, 2, 7, 11, 15], 9) == [1, 3]

    def test_case3(self):
        assert self.sol.twoSum([2, 3, 6, 8, 11, 15], 9) == [2, 3]
