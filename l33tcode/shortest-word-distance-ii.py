from typing import List, Dict


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self._word_to_pos: Dict[str, List[int]] = {}
        self._max_distance = len(wordsDict)

        for pos, word in enumerate(wordsDict):
            self._word_to_pos.setdefault(word, [])
            self._word_to_pos[word].append(pos)

    def shortest(self, word1: str, word2: str) -> int:
        distance = self._max_distance

        left, right = self._word_to_pos[word1], self._word_to_pos[word2]
        pos_left, pos_right = 0, 0

        while pos_left < len(left) and pos_right < len(right):
            distance = min(distance, abs(left[pos_left] - right[pos_right]))
            if left[pos_left] < right[pos_right]:
                pos_left += 1
            else:
                pos_right += 1

        while pos_left < len(left):
            distance = min(distance, abs(left[pos_left] - len(right) + 1))
            pos_left += 1

        while pos_right < len(right):
            distance = min(distance, abs(len(left) - 1 - right[pos_right]))
            pos_right += 1

        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
