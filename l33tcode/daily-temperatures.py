import unittest

class Solution:
    def dailyTemperatures(self, T: 'List[int]') -> 'List[int]':
        day = 0
        stack = []
        result = [0] * len(T)

        while day < len(T):
            while not len(stack) or T[stack[-1]] >= T[day]:
                stack.append(day)
                if day == len(T) - 1:
                    while len(stack):
                        stack.pop()
                    break
                else:
                    day += 1

            while len(stack) and T[stack[-1]] < T[day]:
                tmp_day = stack.pop()
                result[tmp_day] = day - tmp_day

            stack.append(day)
            day += 1

        return result


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_day(self):
        self.assertListEqual(self.sol.dailyTemperatures([31]), [0])

    def test_two_days_asc(self):
        self.assertListEqual(self.sol.dailyTemperatures([31, 32]), [1, 0])

    def test_two_days_desc(self):
        self.assertListEqual(self.sol.dailyTemperatures([70, 32]), [0, 0])

    def test_complex1(self):
        self.assertListEqual(
            self.sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]),
            [1, 1, 4, 2, 1, 1, 0, 0]
        )


if __name__ == "__main__":
    unittest.main()
