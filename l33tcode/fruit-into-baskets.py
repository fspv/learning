import unittest


class Solution:
    def totalFruit(self, tree):
        range_begin = 0
        fruits = 0

        while range_begin < len(tree):
            new_fruits = 0
            mem = dict()
            prev = None

            for pos in range(range_begin, len(tree)):
                if prev != tree[pos]:
                    mem[tree[pos]] = pos

                if len(mem) > 2:
                    break

                prev = tree[pos]
                new_fruits += 1
                fruits = max(fruits, new_fruits)
            else:
                break

            range_begin = mem[prev]

        return fruits


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.totalFruit([]), 0)

    def test_one(self):
        self.assertEqual(self.sol.totalFruit([1]), 1)

    def test_custom1(self):
        self.assertEqual(self.sol.totalFruit([1,1]), 2)

    def test_custom2(self):
        self.assertEqual(self.sol.totalFruit([1,2]), 2)

    def test_custom3(self):
        self.assertEqual(self.sol.totalFruit([1,2,1]), 3)

    def test_custom4(self):
        self.assertEqual(self.sol.totalFruit([0,1,2,2]), 3)

    def test_custom5(self):
        self.assertEqual(self.sol.totalFruit([1,2,3,2,2]), 4)

    def test_custom3(self):
        self.assertEqual(self.sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]), 5)

    def test_custom3(self):
        self.assertEqual(self.sol.totalFruit([1,2,3]), 2)


if __name__ == "__main__":
    unittest.main()
