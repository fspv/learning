import heapq
from collections import Counter


class Word:
    def __init__(self, word: str):
        self._word = word

    def __lt__(self, other):
        return self._word > str(other)

    def __str__(self):
        return self._word


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        index = Counter()

        for word in words:
            index[word] += 1

        for word, count in index.items():
            if len(heap) == k:
                if heap[0] < [count, Word(word)]:
                    heapq.heapreplace(heap, [count, Word(word)])
            else:
                heapq.heappush(heap, [count, Word(word)])

        return reversed([str(heapq.heappop(heap)[1]) for _ in range(k)])
