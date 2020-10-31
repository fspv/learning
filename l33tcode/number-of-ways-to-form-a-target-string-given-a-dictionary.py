from typing import List, Set, Dict
from functools import lru_cache


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7

        if not words:
            return 0

        index: List[Dict[str, int]] = [{} for _ in range(len(words[0]))]

        for word in range(len(words)):
            for pos in range(len(words[word])):
                index[pos].setdefault(words[word][pos], 0)
                index[pos][words[word][pos]] += 1

        @lru_cache(None)
        def dp(word_pos: int, target_pos: int) -> int:
            if target_pos == len(target):
                return 1

            if word_pos == len(words[0]):
                return 0

            count = 0
            if target[target_pos] in index[word_pos]:
                count += (
                    dp(word_pos + 1, target_pos + 1)
                    * index[word_pos][target[target_pos]]
                )

            count += dp(word_pos + 1, target_pos)

            return count % MOD

        return dp(0, 0)
