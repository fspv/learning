class Solution:
    def countArrangement(self, N: int) -> int:
        mem = {}
        n_plus_one = N + 1

        def arrangement(prev, pos, N):
            if pos == n_plus_one:
                return 1

            if pos not in mem:
                mem[pos] = [1]
                for num in range(2, n_plus_one):
                    if pos % num == 0 or num % pos == 0:
                        mem[pos].append(num)

            result = 0
            for num in mem[pos]:
                if num not in prev:
                    prev.add(num)
                    result += arrangement(prev, pos + 1, N)
                    prev.remove(num)

            return result

        result = arrangement(set(), 1, N)

        return result
