from typing import List, Tuple
from collections import deque
from functools import lru_cache


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        def hash_update(pattern_hash: int, remove: int, add: int) -> int:
            pattern_len = 10
            dict_size = 4

            pattern_hash *= dict_size
            pattern_hash -= remove * (dict_size ** pattern_len)
            pattern_hash += add

            return pattern_hash

        @lru_cache(None)
        def letter_to_int(letter: str) -> int:
            return {"A": 0, "C": 1, "G": 2, "T": 3}[letter]

        if len(s) < 10:
            return []

        pattern_hash = 0
        seen = set()

        for pos in range(10):
            pattern_hash = hash_update(pattern_hash, 0, letter_to_int(s[pos]))

        seen.add(pattern_hash)
        added = set()
        result = []

        for pos in range(10, len(s)):
            remove, add = letter_to_int(s[pos - 10]), letter_to_int(s[pos])

            pattern_hash = hash_update(pattern_hash, remove, add)

            if pattern_hash in seen and pattern_hash not in added:
                result.append(s[pos - 9 : pos + 1])
                added.add(pattern_hash)
            else:
                seen.add(pattern_hash)

        return result

    def findRepeatedDnaSequencesSlower1(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        def hash_add(
            dna_hash: Tuple[int, int, int, int], letter: str
        ) -> Tuple[int, int, int, int]:
            letter_hash_map = {"A": 0, "C": 1, "G": 2, "T": 3}

            dna_hash_tmp = list(map(lambda x: x >> 1, dna_hash))
            dna_hash_tmp[letter_hash_map[letter]] |= 1 << 9

            return (dna_hash_tmp[0], dna_hash_tmp[1], dna_hash_tmp[2], dna_hash_tmp[3])

        dna_hash = (0, 0, 0, 0)

        for pos in range(10):
            dna_hash = hash_add(dna_hash, s[pos])

        seen = set()
        seen.add(dna_hash)
        added = set()
        result = []

        for pos in range(10, len(s)):
            dna_hash = hash_add(dna_hash, s[pos])

            if dna_hash in seen and dna_hash not in added:
                result.append(s[pos - 9 : pos + 1])
                added.add(dna_hash)
            else:
                seen.add(dna_hash)

        return result

    def findRepeatedDnaSequencesSlower2(self, s: str) -> List[str]:
        if len(s) < 10:
            return []

        current_subsequence = deque(s[:10])
        current_hash = deque(s[:10])
        seen = set()
        seen.add("".join(current_hash))

        result = set()

        for pos in range(10, len(s)):
            current_subsequence.popleft()
            current_hash.popleft()
            current_subsequence.append(s[pos])
            current_hash.append(s[pos])

            hsh = "".join(current_hash)

            if hsh in seen:
                result.add("".join(current_subsequence))
            else:
                seen.add(hsh)

        return list(result)
