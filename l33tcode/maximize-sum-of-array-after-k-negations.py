import unittest
import heapq

class Solution:
    def largestSumAfterKNegations(self, A, K):
        heapq.heapify(A)
        A_sum = 0

        while K > 0:
            smallest = heapq.heappop(A)
            if smallest < 0:
                K -= 1
                smallest = - smallest
            else:
                K = K % 2
                smallest = smallest * ((-1) ** K)
                K -= 1
            heapq.heappush(A, smallest)

        for elem in A:
            A_sum += elem

        return A_sum

    def largestSumAfterKNegationsBruteForce(self, A, K):
        mem = dict()
        largest = float('-inf') if K % 2 else sum(A)

        for k in range(K % 2, K + 1, 2):
            stack = set()
            stack.add(tuple(0 for _ in range(len(A))))
            while k > 0:
                old_stack = stack
                stack = set()

                for item in old_stack:
                    for pos in range(len(A)):
                        if not item[pos]:
                            new_item = item[:pos] + (1,) + item[pos + 1:]
                            stack.add(new_item)
                            if k == 1:
                                new_item_sum = 0
                                for new_item_pos in range(len(A)):
                                    new_item_sum += \
                                        ((-1) ** new_item[new_item_pos]) * A[new_item_pos]
                                if new_item_sum > largest:
                                    largest = new_item_sum
                k -= 1


        return largest


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_elem(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([0], 1), 0)
        self.assertEqual(self.sol.largestSumAfterKNegations([0], 3), 0)
        self.assertEqual(self.sol.largestSumAfterKNegations([0], 6), 0)
        self.assertEqual(self.sol.largestSumAfterKNegations([1], 1), -1)
        self.assertEqual(self.sol.largestSumAfterKNegations([1], 3), -1)
        self.assertEqual(self.sol.largestSumAfterKNegations([1], 6), 1)

    def test_custom1(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([4,2,3], 1), 5)

    def test_custom2(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([3,-1,0,2], 3), 6)

    def test_custom3(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([2,-3,-1,5,-4], 2), 13)

    def test_custom4(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([-1,-3,8,-6,-9,2,4,0], 8), 33)

    def test_custom5(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([18,-3,28,20,-20,-18,-22,1,-19,14,-19,-19,3,23,-26,-10,-18,15,-27,26,-12,-28,-23,-19,29,-3,-21,-25,-25,-13], 16), 491)

    def test_custom5(self):
        self.assertEqual(self.sol.largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6), 22)


if __name__ == "__main__":
    unittest.main()
