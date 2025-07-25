from collections import deque
from typing import Counter


class Solution:
    def minWindow(self, string: str, pattern: str) -> str:
        chars: Counter[str] = Counter(pattern)

        right = 0

        counter: Counter[str] = Counter()

        min_range = 0, len(string) + 1

        def complete_intersection(this: Counter[str], other: Counter[str]) -> bool:
            for key, value in other.items():
                if this[key] < value:
                    return False

            return True

        for left, char in enumerate(string):
            while right < len(string) and not complete_intersection(counter, chars):
                counter[string[right]] += 1
                right += 1

            if complete_intersection(counter, chars):
                min_range = min(
                    min_range,
                    (left, right),
                    key=lambda interval: interval[1] - interval[0],
                )

            counter[char] -= 1

        if min_range[1] == len(string) + 1:
            return ""

        return string[min_range[0] : min_range[1]]

    def minWindowOld(self, s: str, t: str) -> str:
        result = None
        t_dict = {}

        for pos, sym in enumerate(t):
            if sym in t_dict:
                t_dict[sym].append(-1)
            else:
                t_dict[sym] = deque([-1])

        for pos in range(len(s)):
            if s[pos] in t_dict:
                t_dict[s[pos]].popleft()
                t_dict[s[pos]].append(pos)

                for key in t_dict.keys():
                    if t_dict[key][0] == -1:
                        break
                else:
                    min_val = min([t_dict[key][0] for key in t_dict.keys()])
                    max_val = pos
                    substring = s[min_val : max_val + 1]

                    if result is None or len(substring) < len(result):
                        result = substring

        return "" if result is None else result


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.minWindow("", "") == ""

    def test_one(self):
        assert self.sol.minWindow("A", "A") == "A"

    def test_notexist(self):
        assert self.sol.minWindow("B", "A") == ""
