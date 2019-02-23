import uniitest

# All the solutions run in exactly the same time, but stack requires a
# little bit more memory

class Solution:
    def minAddToMakeValidStack(self, S: str) -> int:
        stack = []

        for s in S:
            if len(stack) and s == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(s)

        return len(stack)

    def minAddToMakeValid(self, S: str) -> int:
        balance = 0
        answer = 0

        for s in S:
            if s == ")":
                balance -= 1
            else:
                balance += 1

            if balance == -1:
                balance = 0
                answer += 1

        return answer + balance


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        self.assertEqual(self.sol.minAddToMakeValid(""), 0)
        self.assertEqual(self.sol.minAddToMakeValid("())"), 1)
        self.assertEqual(self.sol.minAddToMakeValid("((("), 3)
        self.assertEqual(self.sol.minAddToMakeValid("()"), 0)
        self.assertEqual(self.sol.minAddToMakeValid("()))(("), 4)


if __name__ == "__main__":
    unittest.main()
