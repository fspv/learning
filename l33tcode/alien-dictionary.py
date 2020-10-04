from typing import List, DefaultDict, Deque, Dict
from collections import defaultdict, deque


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def construct_adj_list(words: List[str]) -> DefaultDict[str, List[str]]:
            adj_list: DefaultDict[str, List[str]] = defaultdict(list)

            for prefix_len in range(max(map(len, words))):
                prefix_suffix: DefaultDict[str, List[str]] = defaultdict(list)
                for word in words:
                    letter = word[prefix_len] if len(word) > prefix_len else ""

                    if (
                        not prefix_suffix[word[:prefix_len]]
                        or prefix_suffix[word[:prefix_len]][-1] != letter
                    ):
                        prefix_suffix[word[:prefix_len]].append(letter)

                for _, letters in prefix_suffix.items():
                    for letter in letters:
                        adj_list.setdefault(letter, [])

                    for pos in range(1, len(letters)):
                        adj_list[letters[pos - 1]].append(letters[pos])

            for letter in list(adj_list.keys()):
                if letter:
                    adj_list[""].append(letter)

            return adj_list

        def calculate_indegrees(
            adj_list: DefaultDict[str, List[str]]
        ) -> Dict[str, int]:
            indegrees: Dict[str, int] = {}

            for src in adj_list.keys():
                indegrees.setdefault(src, 0)
                for dst in adj_list[src]:
                    indegrees.setdefault(dst, 0)
                    indegrees[dst] += 1

            return indegrees

        def topological_sort(adj_list: DefaultDict[str, List[str]]) -> List[str]:
            queue: Deque[str] = deque()

            for vertex, indegree in indegrees.items():
                if indegree == 0:
                    queue.append(vertex)

            result_list = []

            while queue:
                vertex = queue.popleft()

                result_list.append(vertex)

                for adj_vertex in adj_list[vertex]:
                    indegrees[adj_vertex] -= 1

                    if indegrees[adj_vertex] == 0:
                        queue.append(adj_vertex)

            return result_list

        adj_list = construct_adj_list(words)
        indegrees = calculate_indegrees(adj_list)
        result_list = topological_sort(adj_list)

        if len(result_list) != len(adj_list.keys()):
            return ""

        return "".join(result_list)
