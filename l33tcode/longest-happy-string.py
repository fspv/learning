import heapq
from typing import Dict, List, Optional
from collections import Counter


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        heapq.heappush(heap, (-a, "a"))
        heapq.heappush(heap, (-b, "b"))
        heapq.heappush(heap, (-c, "c"))

        result = ["x", "x"]

        while heap:
            count, char = heapq.heappop(heap)

            if result[-1] == result[-2] == char:
                if heap:
                    count, char = heapq.heapreplace(heap, (count, char))
                else:
                    break

            if count < 0:
                result.append(char)
                count += 1

            if count < 0:
                heapq.heappush(heap, (count, char))

        return "".join(result[2:])


    def longestDiverseStringBruteForce(self, a: int, b: int, c: int) -> str:
        count: Dict[str, int] = Counter()
        count["a"] = a
        count["b"] = b
        count["c"] = c

        def dfs(longest: Dict[str, int], path: List[str], max_len: int) -> str:
            result = ""

            if path and longest[path[-1]] > 2:
                if len(path) - 1 > max_len:
                    return "".join(path[:-1])
                else:
                    return ""

            if count["a"] < 0 or count["b"] < 0 or count["c"] < 0:
                if len(path) - 1 > max_len:
                    return "".join(path[:-1])
                else:
                    return ""

            if count["a"] == 0 and count["b"] == 0 and count["c"] == 0:
                if len(path) > max_len:
                    return "".join(path)
                else:
                    return ""

            for letter in "abc":
                count[letter] -= 1
                path.append(letter)
                result = max(result, dfs(Counter({letter: longest[letter] + 1}), path, len(result)), key=len)
                path.pop()
                count[letter] += 1

            return result

        return "".join(dfs(Counter(), [], 0))
