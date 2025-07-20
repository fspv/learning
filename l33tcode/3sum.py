import unittest


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set = set()
        result = []
        seen = set()

        for pos_left in range(len(nums)):
            if nums[pos_left] in seen:
                continue

            seen.add(nums[pos_left])

            seen_within = set()

            for pos_right in range(pos_left + 1, len(nums)):
                two_sum = -nums[pos_left] - nums[pos_right]

                if two_sum in seen_within:
                    triplet = sorted((nums[pos_left], nums[pos_right], two_sum))
                    triplet_tuple = tuple(triplet)
                    if triplet_tuple not in result_set:
                        result_set.add(triplet_tuple)
                        result.append(triplet)

                seen_within.add(nums[pos_right])

        return result


class Solution1:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        mem_all = {num: set() for num in nums}
        for pos, num in enumerate(nums):
            if len(mem_all[num]) < 3:
                mem_all[num].add(pos)

        nums = []

        for num, positions in mem_all.items():
            for i in range(len(positions)):
                nums.append(num)

        mem_all = {num: set() for num in nums}
        for pos, num in enumerate(nums):
            mem_all[num].add(pos)

        mem_pairs_sums = set()
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                mem_sum_neg = -nums[i] - nums[j]
                # TODO: this one doesn't work properly because set has only
                # unique values so it can easily skip some repeating values.
                # Or need a proof that this is alright
                mem_key = frozenset((nums[i], nums[j], mem_sum_neg))
                if not mem_key in mem_pairs_sums:
                    if mem_sum_neg in mem_all:
                        if len(mem_all[mem_sum_neg] - set([i, j])):
                            mem_pairs_sums.add(mem_key)
                            result.append(
                                [nums[i], nums[j], mem_sum_neg],
                            )

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertListEqual(self.sol.threeSum([]), [])

    def test_zeroes(self):
        self.assertListEqual(self.sol.threeSum([0, 0, 0]), [[0, 0, 0]])

    def test_one(self):
        self.assertListEqual(self.sol.threeSum([1]), [])

    def test_two(self):
        self.assertListEqual(self.sol.threeSum([1, 1]), [])

    def test_three_true(self):
        self.assertListEqual(self.sol.threeSum([1, -1, 0]), [[0, 1, -1]])

    def test_three_false(self):
        self.assertListEqual(self.sol.threeSum([1, 1, 1]), [])

    def test_four_true(self):
        self.assertListEqual(self.sol.threeSum([1, -1, 0, 1]), [[0, 1, -1]])

    def test_four_false(self):
        self.assertListEqual(self.sol.threeSum([1, 1, 1, 1]), [])

    def test_custom1(self):
        self.assertListEqual(
            self.sol.threeSum([-1, 0, 1, 2, -1, -4]), [[0, 1, -1], [2, -1, -1]]
        )

    def test_custom2(self):
        self.assertListEqual(
            self.sol.threeSum([-1, 0, 1, 2, 2, -1, -4]),
            [[0, 1, -1], [2, 2, -4], [2, -1, -1]],
        )


if __name__ == "__main__":
    unittest.main()
