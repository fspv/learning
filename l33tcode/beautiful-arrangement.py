from functools import lru_cache


class Solution:
    def countArrangement(self, N: int) -> int:
        @lru_cache(None)
        def backtrack(pos: int, seen: int) -> int:
            if pos == N:
                return 1

            count = 0

            for num in range(N):
                if (1 << num) & seen > 0:
                    continue
                if (num + 1) % (pos + 1) == 0 or (pos + 1) % (num + 1) == 0:
                    count += backtrack(pos + 1, seen | (1 << num))

            return count

        return backtrack(0, 0)

    def countArrangement1(self, N: int) -> int:
        mem = {}
        visited = [False] * (N + 1)
        n_plus_one = N + 1
        count = [0]

        def arrangement(pos, N):
            if pos == n_plus_one:
                count[0] += 1

            if pos not in mem:
                mem[pos] = [1]
                for num in range(2, n_plus_one):
                    if pos % num == 0 or num % pos == 0:
                        mem[pos].append(num)

            for num in mem[pos]:
                if not visited[num]:
                    visited[num] = True
                    arrangement(pos + 1, N)
                    visited[num] = False

        arrangement(1, N)

        return count[0]
