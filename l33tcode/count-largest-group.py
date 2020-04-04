from collections import Counter


class Solution:
    def countLargestGroup(self, n: int) -> int:
        digt_sum_counter = Counter()
        largest_group = 0

        for num in range(1, n + 1):
            cur_sum = sum(map(int, str(num)))
            digt_sum_counter[cur_sum] += 1
            largest_group = max(largest_group, digt_sum_counter[cur_sum])

        result = 0
        for count in digt_sum_counter.values():
            if count == largest_group:
                result += 1

        return result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.countLargestGroup(13) == 4

    def test_case2(self):
        assert self.sol.countLargestGroup(2) == 2

    def test_case3(self):
        assert self.sol.countLargestGroup(15) == 6

    def test_case4(self):
        assert self.sol.countLargestGroup(24) == 5

    def test_case5(self):
        assert self.sol.countLargestGroup(1000) == 2
