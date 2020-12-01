from typing import List


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        word1_pos, word2_pos = 0, 0
        word1_seen, word2_seen = False, False

        shortest_distance = len(words) + 1

        for pos in range(len(words)):
            if words[pos] == word1:
                word1_pos = pos
                word1_seen = True
            elif words[pos] == word2:
                word2_pos = pos
                word2_seen = True

            if word1_seen and word2_seen:
                shortest_distance = min(shortest_distance, abs(word1_pos - word2_pos))

        return shortest_distance
