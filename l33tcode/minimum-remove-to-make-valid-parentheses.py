class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, to_remove = [], set()

        for pos, char in enumerate(s):
            if char in {"(", ")"}:
                if stack and stack[-1][0] == "(" and char == ")":
                    to_remove.remove(stack.pop()[1])
                else:
                    stack.append((char, pos))
                    to_remove.add(pos)

        return "".join([c for p, c in enumerate(s) if p not in to_remove])


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.minRemoveToMakeValid("") == ""

    def test_one(self):
        assert self.sol.minRemoveToMakeValid("a") == "a"

    def test_case1(self):
        assert self.sol.minRemoveToMakeValid("()") == "()"

    def test_case2(self):
        assert self.sol.minRemoveToMakeValid("())") == "()"

    def test_case3(self):
        assert self.sol.minRemoveToMakeValid("))") == ""

    def test_case4(self):
        assert self.sol.minRemoveToMakeValid("(") == ""

    def test_case5(self):
        assert self.sol.minRemoveToMakeValid("lee(t(c)o)de)") == "lee(t(c)o)de"

    def test_case6(self):
        assert self.sol.minRemoveToMakeValid("a)b(c)d") == "ab(c)d"

    def test_case7(self):
        assert self.sol.minRemoveToMakeValid("))((") == ""

    def test_case8(self):
        assert self.sol.minRemoveToMakeValid("(a(b(c)d)") == "a(b(c)d)"
