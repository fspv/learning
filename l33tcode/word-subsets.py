from typing import List, Counter


class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def is_subset(word1: Counter[str], word2: Counter[str]) -> bool:
            for key, value in word1.items():
                if word2[key] < value:
                    return False

            return True

        counter_b: Counter[str] = Counter()

        for cur_counter_b in map(lambda x: Counter(x), set(B)):
            for key, value in cur_counter_b.items():
                counter_b[key] = max(counter_b[key], value)

        counters_a = list(map(lambda x: Counter(x), A))

        result: List[str] = []

        for pos, counter_a in enumerate(counters_a):
            if is_subset(counter_b, counter_a):
                result.append(A[pos])

        return result
