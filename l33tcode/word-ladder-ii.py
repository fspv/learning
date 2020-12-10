import heapq
from typing import List, Tuple, Dict, DefaultDict, Set, Deque
from collections import defaultdict, deque


class Solution:
    def findLadders(
        self, begin_word: str, end_word: str, words: List[str]
    ) -> List[List[str]]:
        words.append(begin_word)
        words_extended = words  # Ideally should be copied, but referencing for performance

        words_extended_pos: Dict[str, int] = {v: k for k, v in enumerate(words_extended)}

        begin_word_pos = len(words_extended) - 1
        end_word_pos = -1

        # Build adjacency list
        adj_list: List[List[int]] = [[] for _ in range(len(words_extended))]
        for word in range(len(words_extended)):
            if words_extended[word] == end_word:
                end_word_pos = word

            string_list = list(words_extended[word])
            for pos in range(len(string_list)):
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    tmp = string_list[pos]
                    string_list[pos] = letter
                    adj_word = "".join(string_list)
                    string_list[pos] = tmp
                    if adj_word in words_extended_pos:
                        adj_word_pos = words_extended_pos[adj_word]
                        adj_list[word].append(adj_word_pos)
                        adj_list[adj_word_pos].append(word)

        if end_word_pos == -1:
            return []

        # BFS
        distances: List[float] = [len(words_extended) + 10] * len(words_extended)
        distances[begin_word_pos] = 0

        parents: List[Set[int]] = [set() for _ in range(len(words_extended))]

        queue: Deque[int] = deque()
        queue.append(begin_word_pos)

        while queue:
            word = queue.popleft()
            if word == end_word_pos:
                break

            for adj_word in adj_list[word]:
                adj_distance = distances[word] + 1

                if adj_distance < distances[adj_word]:
                    distances[adj_word] = adj_distance
                    parents[adj_word].add(word)
                    queue.append(adj_word)
                elif adj_distance == distances[adj_word]:
                    parents[adj_word].add(word)

        if distances[end_word_pos] > len(words) + 2:
            return []

        result: List[List[str]] = []

        def dfs(word: int, path: List[str]) -> None:
            if word == begin_word_pos:
                result.append(list(reversed(path)))

            for parent in parents[word]:
                path.append(words_extended[parent])
                dfs(parent, path)
                path.pop()

        dfs(end_word_pos, [end_word])

        return result
