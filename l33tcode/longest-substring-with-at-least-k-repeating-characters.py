from typing import Counter


class CharLessThanK:
    def __init__(self, k: int) -> None:
        self.k = k
        self.counter: Counter[str] = Counter()
        self.count = 0

    def add(self, char: str) -> None:
        if self.counter[char] == 0:
            self.count += 1

        self.counter[char] += 1

        if self.counter[char] == self.k:
            self.count -= 1

    def remove(self, char: str) -> None:
        if self.counter[char] == self.k:
            self.count += 1

        self.counter[char] -= 1

        if self.counter[char] == 0:
            self.count -= 1
            self.counter.pop(char)


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        longest_substring = 0

        for chars in range(1, len(set(s)) + 1):
            start, end = 0, 0
            counter = CharLessThanK(k)
            while end < len(s):
                counter.add(s[end])

                while len(counter.counter.keys()) > chars:
                    counter.remove(s[start])
                    start += 1

                end += 1

                if counter.count == 0:
                    longest_substring = max(longest_substring, end - start)

        return longest_substring


    def longestSubstringBruteForce(self, s: str, k: int) -> int:
        longest_substring = 0

        start, end = 0, 0
        counter = CharLessThanK(k)

        while start < len(s):
            while end < len(s):
                counter.add(s[end])

                end += 1

                if counter.count == 0:
                    longest_substring = max(longest_substring, end - start)

            while counter.count > 0:
                counter.remove(s[end - 1])
                end -= 1

            counter.remove(s[start])

            start += 1

        return longest_substring
