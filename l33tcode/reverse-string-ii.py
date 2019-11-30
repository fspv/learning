class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(start, end, arr):
            while start < end:
                arr[end], arr[start] = arr[start], arr[end]
                start += 1
                end -= 1

        def process_interval(start, end, arr):
            center = min(len(arr), (end + start) // 2)

            reverse(start, center - 1, arr)

        arr = list(s)

        for pos in range(0, len(s), 2 * k):
            process_interval(pos, pos + 2 * k, arr)

        return "".join(arr)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.reverseStr("", 1) == ""
        assert self.sol.reverseStr("", 3) == ""

    def test_case1(self):
        assert self.sol.reverseStr("ab", 1) == "ab"

    def test_case2(self):
        assert self.sol.reverseStr("ab", 2) == "ba"

    def test_case3(self):
        assert self.sol.reverseStr("abcdefg", 2) == "bacdfeg"
