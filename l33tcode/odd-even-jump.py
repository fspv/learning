from functools import lru_cache


class Solution:
    def next_higher_compute(self, arr):
        stack = []
        self._next_higher = list(range(len(arr)))
        for _, pos in sorted(((n, p) for p, n in enumerate(arr))):
            while stack and stack[-1] < pos:
                self._next_higher[stack.pop()] = pos

            stack.append(pos)

    def next_lower_compute(self, arr):
        stack = []
        self._next_lower = list(range(len(arr)))
        for _, pos in sorted(((-n, p) for p, n in enumerate(arr))):
            while stack and stack[-1] < pos:
                self._next_lower[stack.pop()] = pos

            stack.append(pos)

    def oddEvenJumps(self, A: List[int]) -> int:
        self.next_higher_compute(A)
        self.next_lower_compute(A)

        dp = [[False, False] for _ in A]
        dp[-1] = [True, True]  # 0 - can reach end via odd jump, 1 - via even

        for pos in reversed(range(len(A))):
            if self._next_higher[pos] != pos:
                dp[pos][0] = dp[self._next_higher[pos]][1]
            if self._next_lower[pos] != pos:
                dp[pos][1] = dp[self._next_lower[pos]][0]

        return sum(p[0] for p in dp)

    def oddEvenJumpsTopDown(self, A: List[int]) -> int:
        @lru_cache(None)
        def dfs(pos: int, odd: bool) -> bool:
            """
            @param odd - True if odd, False if even
            """

            if pos == len(A) - 1:
                return True

            if odd:
                new_pos = self._next_higher[pos]
            else:
                new_pos = self._next_lower[pos]

            if new_pos != pos:
                return dfs(new_pos, not odd)

            return False

        self.next_higher_compute(A)
        self.next_lower_compute(A)

        good_indexes = 0
        for pos in range(len(A)):
            if dfs(pos, True):
                good_indexes += 1

        return good_indexes
