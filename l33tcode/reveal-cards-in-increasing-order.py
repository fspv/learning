import unittest
from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        queue = deque(range(len(deck)))
        out = [None] * len(deck)

        for elem in sorted(deck):
            pos = queue.popleft()
            out[pos] = elem
            if queue:
                pos = queue.popleft()
                queue.append(pos)

        return out


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertEqual(self.sol.deckRevealedIncreasing([]), [])

    def test_one(self):
        self.assertEqual(self.sol.deckRevealedIncreasing([2]), [2])

    def test_two1(self):
        self.assertEqual(self.sol.deckRevealedIncreasing([1, 2]), [1, 2])

    def test_two2(self):
        self.assertEqual(self.sol.deckRevealedIncreasing([2, 1]), [1, 2])

    def test_custom(self):
        self.assertEqual(self.sol.deckRevealedIncreasing([17,13,11,2,3,5,7]), [2,13,3,11,5,17,7])


if __name__ == "__main__":
    unittest.main()
