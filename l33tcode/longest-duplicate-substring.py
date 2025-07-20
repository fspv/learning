from typing import List
from collections import defaultdict
from functools import reduce


class Solution:
    def longestDupSubstring(self, S: str) -> str:
        class RollingHash:
            def __init__(self, nums: List[int]) -> None:
                self._hash = 0
                self._mod = 2 << 63 - 1
                self._pow = 26 ** (len(nums) - 1) % self._mod

                for num in nums:
                    self.append(num)

            def append(self, num: int) -> None:
                self._hash = (self._hash * 26 + num) % self._mod

            def popleft(self, num: int) -> None:
                self._hash -= self._pow * num

            def __hash__(self) -> int:
                return self._hash

        def check_matches(nums: List[int], size: int) -> int:
            rolling_hash = RollingHash(nums[:size])
            seen = defaultdict(list)

            for pos in range(1, len(nums) - size + 1):
                seen[hash(rolling_hash)].append(pos - 1)

                rolling_hash.popleft(nums[pos - 1])
                rolling_hash.append(nums[pos + size - 1])

                if hash(rolling_hash) in seen:
                    # Double check, if we have a collision.
                    # In this task we don't have collisions, so this just
                    # increasing running time
                    for prev_pos in seen[hash(rolling_hash)]:
                        if S[prev_pos : prev_pos + size] == S[pos : pos + size]:
                            return pos

            return -1

        def bisect(S: str) -> str:
            left, right = 0, len(S)

            start, size = 0, 0

            nums = [ord(c) - ord("a") for c in S]

            while (middle := (left + right) // 2) != left:
                if (match := check_matches(nums, middle)) != -1:
                    left = middle
                    start, size = match, middle
                else:
                    right = middle

            return S[start : start + size]

        return bisect(S)

    def longestDupSubstringFast(self, S: str) -> str:
        mod = 2 ** 63 - 1

        def check_matches(nums: List[int], size: int) -> int:
            rolling_hash = reduce(lambda x, y: (x * 26 + y) % mod, nums[:size], 0)
            most_significant = (26 ** size) % mod
            seen = {rolling_hash}

            for pos in range(1, len(nums) - size + 1):
                rolling_hash = (
                    rolling_hash * 26
                    - most_significant * nums[pos - 1]
                    + nums[pos + size - 1]
                ) % mod

                if rolling_hash in seen:
                    return pos

                seen.add(rolling_hash)

            return -1

        def bisect(S: str) -> str:
            left, right = 0, len(S) - 1

            start, size = 0, 0

            nums = [ord(c) - ord("a") for c in S]

            while (middle := (left + right) // 2) != left:
                if (match := check_matches(nums, middle)) != -1:
                    left = middle
                    start, size = match, middle
                else:
                    right = middle

            return S[start : start + size]

        return bisect(S)

    def longestDupSubstringBruteForce(self, S: str) -> str:
        char_to_pos = defaultdict(list)

        for pos, char in enumerate(S):
            char_to_pos[char].append(pos)

        def match_from_pos(left, right, S):
            match = 0
            while left < len(S) and right < len(S) and S[left] == S[right]:
                left += 1
                right += 1
                match += 1

            return match

        max_match, start, end = 0, 0, 0
        for positions in char_to_pos.values():
            for left in range(len(positions)):
                for right in range(left + 1, len(positions)):
                    match = match_from_pos(positions[left], positions[right], S)

                    if match > max_match:
                        max_match, start, end = (
                            match,
                            positions[left],
                            positions[left] + match,
                        )

        return S[start:end]


class TestSolution:
    def setup(self):
        self.sol = Solution()
