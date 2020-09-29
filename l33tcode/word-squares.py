from typing import Dict, List, Set, Tuple
from functools import lru_cache


class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        def gen_word_by_first(words: List[str]) -> Dict[str, Set[int]]:
            result: Dict[str, Set[int]] = {}

            result[""] = list(range(len(words)))

            for pos in range(len(words)):
                for prefix in range(len(words[pos])):
                    result.setdefault(words[pos][:prefix + 1], set())
                    result[words[pos][:prefix + 1]].add(pos)

            return result

        result: List[List[int]] = []
        word_by_first: Dict[str, Set[int]] = gen_word_by_first(words)
        path: List[int] = []

        def validate_row(row: int, path: List[int]) -> bool:
            for col in range(row + 1):
                if words[path[row]][col] != words[path[col]][row]:
                    return False

            return True

        def dfs(pos: int) -> None:
            if pos == len(words[0]):
                result.append(path.copy())
                return

            prefix = "".join([words[p][pos] for p in path])

            for word in word_by_first.get(prefix, set()):
                path.append(word)
                if validate_row(pos, path):
                    dfs(pos + 1)
                path.pop()

        dfs(0)

        return [[words[p] for p in r] for r in result]
