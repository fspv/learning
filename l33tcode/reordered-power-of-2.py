from typing import Set, Tuple


class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        def get_combinations() -> Set[Tuple[str]]:
            result: Set[Tuple[str]] = set()

            n = 1
            for _ in range(32):
                result.add(tuple(sorted(str(int(n)))))
                n <<= 1

            return result

        combinations = get_combinations()

        sorted_number = tuple(sorted(str(N)))

        return sorted_number in combinations
