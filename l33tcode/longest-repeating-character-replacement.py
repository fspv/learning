from collections import defaultdict
from functools import cache
from typing import DefaultDict, List


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        def build_char_map() -> DefaultDict[str, List[int]]:
            result: DefaultDict[str, List[int]] = defaultdict(list)

            for pos, char in enumerate(s):
                result[char].append(pos)

            return result

        char_map: DefaultDict[str, List[int]] = build_char_map()

        max_length = 0

        for positions in char_map.values():
            # Sliding window algorithm
            left, right = 0, 0
            length = 1
            replacements = k

            max_length = max(max_length, 1 + min(replacements, len(s) - 1))

            while right < len(positions) - 1:
                diff = positions[right + 1] - positions[right] - 1

                if replacements - diff >= 0:
                    length += diff + 1
                    replacements -= diff

                    max_length = max(
                        max_length,
                        length
                        + min(
                            replacements,
                            len(s) - positions[right + 1] - 1 + positions[0],
                        ),
                    )

                    right += 1
                elif left == right:
                    left += 1
                    right += 1
                else:
                    diff = positions[left + 1] - positions[left] - 1

                    length -= diff + 1
                    replacements += diff

                    left += 1

        return max_length

    def characterReplacementDPOptimized(self, s: str, k: int) -> int:
        # FIXME: incorrect (doesn't take into account ABBB, 1 -> 4)
        def build_char_map() -> DefaultDict[str, List[int]]:
            result: DefaultDict[str, List[int]] = defaultdict(list)

            for pos, char in enumerate(s):
                result[char].append(pos)

            return result

        @cache
        def dp(char: str, pos: int, left: int) -> int:
            max_length_local = max(
                1, min(len(s) - positions[pos] + positions[0], left + 1)
            )

            for next_pos in range(pos + 1, len(positions)):
                diff = positions[next_pos] - positions[pos] - 1
                if diff <= left:
                    max_length_local = max(
                        max_length_local, dp(char, next_pos, left - diff) + 1 + diff
                    )

            return max_length_local

        char_map: DefaultDict[str, List[int]] = build_char_map()

        max_length = 0

        for char, positions in char_map.items():

            max_length = max(
                max_length, max(dp(char, pos, k) for pos in range(len(positions)))
            )

        return max_length

    def characterReplacementDP(self, s: str, k: int) -> int:
        # FIXME: incorrect (doesn't take into account ABBB, 1 -> 4)
        @cache
        def dp(pos: int, left: int) -> int:
            if len(s) == pos:
                return left

            max_length = max(1, min(left + 1, len(s) - pos))

            for next_pos in range(pos + 1, min(pos + left + 2, len(s) + 1)):
                if next_pos == len(s) or s[pos] == s[next_pos]:
                    replacements = next_pos - pos - 1
                    max_length = max(
                        max_length, dp(next_pos, left - replacements) + replacements + 1
                    )

            return max_length

        return min(max(dp(pos, k) for pos in range(len(s))), len(s))
