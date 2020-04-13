from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def find(array: List[int], pos: int):
            root = pos

            while array[root] != root:
                root = array[root]

            while array[pos] != root:
                array[pos], pos = root, array[pos]

            return root

        def union(root_left: int, root_right: int, count: List[int], array: List[int]):
            root_less, root_more = tuple(
                sorted([root_left, root_right], key=lambda x: count[x])
            )
            array[root_less] = root_more
            count[root_more] += count[root_less]

        union_find = list(range(len(nums)))
        num_to_pos = {v: k for k, v in enumerate(nums)}
        count = [1] * len(nums)

        for num in nums:
            for neigh in [num - 1, num + 1]:
                if neigh not in num_to_pos:
                    continue

                root_left, root_right = (
                    find(union_find, num_to_pos[neigh]),
                    find(union_find, num_to_pos[num]),
                )

                if root_left != root_right:
                    union(root_left, root_right, count, union_find)

        return max(count) if count else 0


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.longestConsecutive([]) == 0

    def test_case1(self):
        assert self.sol.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4

    def test_case2(self):
        assert self.sol.longestConsecutive([1, 0, -1]) == 3
