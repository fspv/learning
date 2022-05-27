from typing import Dict, List


class Solution:
    def evaluate(self, string: str, knowledge: List[List[str]]) -> str:
        left, right = 0, 0

        word_map: Dict[str, str] = {k: v for k, v in knowledge}

        result: List[str] = []

        while left < len(string):
            if string[left] != "(":
                result.append(string[left])
                left += 1
                right = left
                continue

            right += 1  # skip "("

            # Scan Until ")"
            word: List[str] = []
            while right < len(string) and string[right] != ")":
                word.append(string[right])
                right += 1

            # Check if there is mapping and update the result
            if "".join(word) in word_map:
                result.extend(list(word_map["".join(word)]))
            else:
                result.append("?")

            # Move pointers to scan further
            left = right + 1
            right = left

        return "".join(result)
