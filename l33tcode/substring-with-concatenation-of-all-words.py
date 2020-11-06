from typing import List, Set, Dict
from collections import defaultdict, Counter


class RollingHash:
    def __init__(self) -> None:
        self._hash = 0
        self._length = 0
        self._base = ord("z") - ord("a") + 1

    def add(self, char: str) -> None:
        self._hash *= self._base
        self._hash += ord(char) - ord("a")
        self._length += 1

    def popleft(self) -> None:
        if self._length == 0:
            raise RuntimeError("Nothing to remove")

        self._length -= 1
        self._hash %= self._base ** self._length

    @property
    def value(self) -> int:
        return self._hash


class Solution:
    def findSubstringBruteForce(self, string: str, words: List[str]) -> List[int]:
        matches = defaultdict(list)

        dp: List[List[int]] = [[] for _ in range(len(string))]

        for word in range(len(words)):
            for pos in range(len(string)):
                if string[pos : pos + len(words[word])] == words[word]:
                    matches[words[word]].append(pos)
                    dp[pos].append(word)

        def dfs(pos: int, seen: Set[int]) -> bool:
            if len(seen) == len(words):
                return True

            if pos == len(string):
                return False

            for word in dp[pos]:
                if word not in seen:
                    seen.add(word)
                    if dfs(pos + len(words[word]), seen):
                        return True
                    seen.remove(word)

            return False

        result = []

        for pos in range(len(string)):
            if dfs(pos, set()):
                result.append(pos)

        return result

    def findSubstring(self, string: str, words: List[str]) -> List[int]:
        hashes = [0] * len(string)
        word_len = len(words[0]) if words else 0
        rolling_hash = RollingHash()

        for pos in range(len(string) + 1):
            if pos >= word_len:
                hashes[pos - word_len] = rolling_hash.value

            if pos < len(string):
                rolling_hash.add(string[pos])

            if pos >= word_len:
                rolling_hash.popleft()

        hash_counter: Dict[int, int] = Counter()

        for word in words:
            word_rolling_hash = RollingHash()
            for char in word:
                word_rolling_hash.add(char)
            hash_counter[word_rolling_hash.value] += 1

        total = len(words)

        def dfs(pos: int) -> bool:
            nonlocal total
            if total == 0:
                return True

            if pos >= len(string):
                return False

            if hash_counter[hashes[pos]] > 0:
                hash_counter[hashes[pos]] -= 1
                total -= 1
                if dfs(pos + word_len):
                    hash_counter[hashes[pos]] += 1
                    total += 1
                    return True
                hash_counter[hashes[pos]] += 1
                total += 1

            return False

        result = []

        for pos in range(len(string) - word_len * len(words) + 1):
            if dfs(pos):
                result.append(pos)

        return result
