import unittest

class Solution:
    def shipWithinDays(self, weights, D):
        left, right = min(weights), sum(weights) + 1

        while right - left > 1:
            middle = int((left + right) / 2)

            days = 0
            sum_weight = 0

            for weight in weights:
                if sum_weight + weight > middle:
                    if weight > middle:
                        days = float("inf")
                        break
                    else:
                        days += 1
                        sum_weight = weight
                else:
                    sum_weight += weight
            else:
                days += 1

            if days > D:
                left = middle
            else:
                right = middle

        return right


    def shipWithinDaysBruteForce(self, weights, D):
        # Almost works IMO. But I won't fix it.
        seps = [n for n in range(D)]
        seps[-1] = len(weights) - 1
        seps_weights = [weights[n] for n in range(D)]
        seps_weights[-1] += sum(weights[D:])

        stack = [(seps, seps_weights, 0)]

        min_ship = float("inf")

        while stack:
            if weights[0] == 147:
                from pprint import pprint
                pprint(stack, indent=8)
            seps, seps_weights, sep = stack[-1]
            max_weight = max(seps_weights)
            min_ship = max_weight if min_ship > max_weight else min_ship

            if sep < D - 1 and seps[sep] < len(weights):
                if seps[sep + 1] - seps[sep] > 1:
                    seps[sep] += 1
                    seps_weights[sep] += weights[seps[sep]]
                    seps_weights[sep + 1] -= weights[seps[sep]]
                    stack.append((seps, seps_weights, 0))
                else:
                    stack.pop()
                    stack.append((seps, seps_weights, sep + 1))
            else:
                stack.pop()

        return min_ship


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_custom1(self):
        self.assertEqual(self.sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5), 15)

    def test_custom2(self):
        self.assertEqual(self.sol.shipWithinDays([3,2,2,4,1,4], 3), 6)

    def test_custom3(self):
        self.assertEqual(self.sol.shipWithinDays([1,2,3,1,1], 4), 3)

    def test_custom4(self):
        self.assertEqual(self.sol.shipWithinDays([1,2,3,1], 4), 3)

    def test_custom5(self):
        self.assertEqual(self.sol.shipWithinDays([147,73,265,305,191,152,192,293,309,292,182,157,381,287,73,162,313,366,346,47], 10), 602)


if __name__ == "__main__":
    unittest.main()
