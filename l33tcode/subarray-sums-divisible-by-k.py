from collections import Counter

class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        sums = [0]

        for num in A:
            sums.append((sums[-1] + num) % K)

        counter = Counter(sums)

        return int(sum(n * (n - 1) / 2 for n in counter.values()))
