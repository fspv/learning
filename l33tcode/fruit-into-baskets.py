import unittest


class Solution:
    def totalFruit(self, tree):
        range_begin = 0
        fruits = 0
        new_fruits = 0
        mem = dict()

        while range_begin < len(tree):
            prev = None

            for pos in range(range_begin, len(tree)):
                if prev != tree[pos]:
                    mem[tree[pos]] = pos

                if len(mem) > 2:
                    range_begin = pos
                    new_fruits = pos - mem[prev]
                    mem = {prev: mem[prev]}
                    break

                prev = tree[pos]
                new_fruits += 1
                fruits = max(fruits, new_fruits)
            else:
                break

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

    def test_custom6(self):
        self.assertEqual(self.sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]), 5)

    def test_custom7(self):
        self.assertEqual(self.sol.totalFruit([1,2,3]), 2)

    def test_custom8(self):
        self.assertEqual(self.sol.totalFruit([1,0,3,4,3]), 3)


if __name__ == "__main__":
    unittest.main()
