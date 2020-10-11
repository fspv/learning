import collections
from typing import List, Set, Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack: List[str] = []
        added: Set[str] = set()
        counter: Counter[str] = collections.Counter(s)

        for pos in range(len(s)):
            counter[s[pos]] -= 1

            if s[pos] in added:
                continue

            while stack and stack[-1] > s[pos]:
                if counter[stack[-1]] > 0:
                    removed = stack.pop()
                    added.remove(removed)
                else:
                    break

            added.add(s[pos])
            stack.append(s[pos])

        return "".join(stack)
