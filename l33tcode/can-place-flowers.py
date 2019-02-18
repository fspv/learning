import unittest

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = n

        if count == 0:
            return True

        plot = 0

        while plot < len(flowerbed):
            if plot - 1 < 0 or not flowerbed[plot - 1]:
                if plot + 1 >= len(flowerbed) or not flowerbed[plot + 1]:
                    if not flowerbed[plot]:
                        flowerbed[plot] = 1
                        count -= 1

                        if count == 0:
                            return True
                    plot += 1
                else:
                    plot += 2
            plot += 1

        return False


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty(self):
        self.assertTrue(self.sol.canPlaceFlowers([], 0))
        self.assertFalse(self.sol.canPlaceFlowers([], 1))
        self.assertFalse(self.sol.canPlaceFlowers([], 5))

    def test_one_elem(self):
        self.assertTrue(self.sol.canPlaceFlowers([0], 0))
        self.assertTrue(self.sol.canPlaceFlowers([0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0], 7))
        self.assertTrue(self.sol.canPlaceFlowers([1], 0))
        self.assertFalse(self.sol.canPlaceFlowers([1], 1))
        self.assertFalse(self.sol.canPlaceFlowers([1], 6))

    def test_two_elements(self):
        self.assertTrue(self.sol.canPlaceFlowers([0, 0], 0))
        self.assertTrue(self.sol.canPlaceFlowers([0, 0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0, 0], 2))
        self.assertFalse(self.sol.canPlaceFlowers([0, 0], 5))
        self.assertTrue(self.sol.canPlaceFlowers([1, 0], 0))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0], 2))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0], 5))
        self.assertTrue(self.sol.canPlaceFlowers([0, 1], 0))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1], 2))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1], 5))

    def test_three_elements(self):
        self.assertTrue(self.sol.canPlaceFlowers([0, 0, 0], 0))
        self.assertTrue(self.sol.canPlaceFlowers([0, 0, 0], 1))
        self.assertTrue(self.sol.canPlaceFlowers([0, 0, 0], 2))
        self.assertFalse(self.sol.canPlaceFlowers([0, 0, 0], 5))
        self.assertTrue(self.sol.canPlaceFlowers([1, 0, 0], 0))
        self.assertTrue(self.sol.canPlaceFlowers([1, 0, 0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0, 0], 2))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0, 0], 5))
        self.assertTrue(self.sol.canPlaceFlowers([0, 1, 0], 0))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1, 0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1, 0], 2))
        self.assertFalse(self.sol.canPlaceFlowers([0, 1, 0], 5))
        self.assertTrue(self.sol.canPlaceFlowers([0, 0, 1], 0))
        self.assertTrue(self.sol.canPlaceFlowers([0, 0, 1], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0, 0, 1], 2))
        self.assertFalse(self.sol.canPlaceFlowers([0, 0, 1], 5))

    def test_three_custom1(self):
        self.assertTrue(self.sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))
        self.assertFalse(self.sol.canPlaceFlowers([1, 0, 0, 0, 1], 2))

    def test_three_custom2(self):
        self.assertTrue(self.sol.canPlaceFlowers([0,1,0,1,0,1,0,0], 0))
        self.assertTrue(self.sol.canPlaceFlowers([0,1,0,1,0,1,0,0], 1))
        self.assertFalse(self.sol.canPlaceFlowers([0,1,0,1,0,1,0,0], 2))

if __name__ == "__main__":
    unittest.main()
