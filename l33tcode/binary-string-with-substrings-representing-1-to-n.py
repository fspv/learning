from typing import Set


class Solution:
    def queryString(self, S: str, N: int) -> bool:
        seen: Set[int] = set()

        for start in range(len(S)):
            rolling_hash = 0
            end = start

            for end in range(start, len(S)):
                rolling_hash <<= 1
                rolling_hash += int(S[end])

                if rolling_hash <= N:
                    seen.add(rolling_hash)
                else:
                    break

        seen.discard(0)

        return len(seen) == N
