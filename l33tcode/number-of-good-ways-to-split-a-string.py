from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        counter_left, counter_right = Counter(), Counter(s)

        num_splits = 0

        for char in s:
            counter_left[char] += 1

            if counter_right[char] > 1:
                counter_right[char] -= 1
            else:
                del counter_right[char]

            if len(counter_left) == len(counter_right):
                num_splits += 1

        return num_splits
