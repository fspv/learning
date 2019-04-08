import unittest


class Solution:
    def real_value(self, string, pos):
        if pos < 0 or string[pos] != "#":
            return pos

        backspace_count = 0
        while string[pos] == "#":
            backspace_count += 1
            pos -= 1

        for _ in range(backspace_count):
            pos = self.real_value(string, pos - 1)

        return pos

    def backspaceCompare(self, S, T):
        S_ptr = len(S) - 1
        T_ptr = len(T) - 1

        while S_ptr >= 0 or T_ptr >= 0:
            S_ptr, T_ptr = self.real_value(S, S_ptr), self.real_value(T, T_ptr)

            if S_ptr >= 0 and T_ptr >= 0:
                if S[S_ptr] != T[T_ptr]:
                    return False
            elif S_ptr >= 0 or T_ptr >= 0:
                return False

            S_ptr -= 1
            T_ptr -= 1

        return True


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_empty1(self):
        self.assertEqual(self.sol.backspaceCompare("", ""), True)

    def test_empty2(self):
        self.assertEqual(self.sol.backspaceCompare("", "a#"), True)

    def test_empty3(self):
        self.assertEqual(self.sol.backspaceCompare("a#", "a#"), True)

    def test_empty4(self):
        self.assertEqual(self.sol.backspaceCompare("a#", ""), True)

    def test_empty5(self):
        self.assertEqual(self.sol.backspaceCompare("a#", "a"), False)

    def test_empty6(self):
        self.assertEqual(self.sol.backspaceCompare("ab##", "c#d#"), True)

    def test_custom1(self):
        self.assertEqual(self.sol.backspaceCompare("a##c", "#a#c"), True)

    def test_custom2(self):
        self.assertEqual(self.sol.backspaceCompare("a#c", "b"), False)

    def test_custom3(self):
        self.assertEqual(self.sol.backspaceCompare("abcdef#gh", "abcdef#f#f#f#ghvg##"), True)

    def test_custom4(self):
        self.assertEqual(self.sol.backspaceCompare("bxj##tw", "bxj###tw"), False)

    def test_custom5(self):
        self.assertEqual(self.sol.backspaceCompare("bbbextm", "bbb#extm"), False)


if __name__ == "__main__":
    unittest.main()
