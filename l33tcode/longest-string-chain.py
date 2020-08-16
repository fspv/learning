from typing import List, Dict
from functools import lru_cache
from collections import defaultdict


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def one_letter_apart(pos_word_left: int, pos_word_right: int) -> bool:
            distance = 0
            word_left, word_right = words[pos_word_left], words[pos_word_right]
            pos_left, pos_right = 0, 0

            while (
                distance < 2
                and pos_left < len(word_left)
                and pos_right < len(word_right)
            ):
                if word_left[pos_left] == word_right[pos_right]:
                    pos_left += 1
                    pos_right += 1
                else:
                    distance += 1
                    pos_right += 1

            distance += len(word_right) - pos_right

            return distance == 1

        words.sort(key=len)
        word_len_range: Dict[int, List[int]] = defaultdict(lambda: [0, 0])

        for pos, word in enumerate(words):
            if len(word) not in word_len_range:
                word_len_range[len(word)] = [pos, pos + 1]
            else:
                word_len_range[len(word)][1] = pos + 1

        dp = [1] * len(words)

        for start in reversed(range(len(words))):
            for next_word in range(*word_len_range[len(words[start]) + 1]):
                if one_letter_apart(start, next_word):
                    dp[start] = max(dp[start], dp[next_word] + 1,)

        return max(dp)

    def longestStrChainTopDown(self, words: List[str]) -> int:
        @lru_cache(None)
        def one_letter_apart(word_left: int, word_right: int) -> bool:
            def one_letter_apart_dfs(
                pos_left: int, pos_right: int, distance: int
            ) -> bool:
                # print(words[word_left], words[word_right], pos_left, pos_right)
                if distance > 1:
                    return False

                if pos_left == len(words[word_left]) and pos_right == len(
                    words[word_right]
                ):
                    return True
                elif (
                    pos_left < len(words[word_left])
                    and words[word_left][pos_left] == words[word_right][pos_right]
                ):
                    if one_letter_apart_dfs(pos_left + 1, pos_right + 1, distance):
                        return True
                else:
                    if one_letter_apart_dfs(pos_left, pos_right + 1, distance + 1):
                        return True

                return False

            return one_letter_apart_dfs(0, 0, 0)

        words.sort(key=len)
        word_len_range: Dict[int, List[int]] = defaultdict(lambda: [0, 0])

        for pos, word in enumerate(words):
            if len(word) not in word_len_range:
                word_len_range[len(word)] = [pos, pos + 1]
            else:
                word_len_range[len(word)][1] = pos + 1

        def dfs(start: int) -> int:
            # the longest sequence from here
            result = 1

            for next_word in range(*word_len_range[len(words[start]) + 1]):
                # print(start, next_word, word_len_range)
                if one_letter_apart(start, next_word):
                    result = max(result, dfs(next_word) + 1)

            return result

        result = 0
        for start in reversed(range(len(words))):
            result = max(result, dfs(start))

        return result
