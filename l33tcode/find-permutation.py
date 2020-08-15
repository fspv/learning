from typing import Set, List, Optional


class Direction:
    INCREASING = "I"
    DECREASING = "D"


class Solution:
    def findPermutation(self, s: str) -> List[int]:
        def going_up(direction: str) -> bool:
            return direction == Direction.INCREASING

        numbers = list(reversed(range(1, len(s) + 3)))

        stack: List[int] = [numbers.pop()]
        result: List[int] = []

        for direction in s + Direction.INCREASING:
            if going_up(direction):
                while stack:
                    result.append(stack.pop())
            stack.append(numbers.pop())

        return result

    def findPermutationBruteforce(self, s: str) -> List[int]:
        def direction_matches(prev_num: int, next_num: int, direction: str) -> bool:
            if direction == Direction.INCREASING:
                return prev_num < next_num
            else:
                return prev_num > next_num

        def dfs(sig_pos: int, left: Set[int], path: List[int]) -> Optional[List[int]]:
            if sig_pos == len(s):
                return path.copy()

            for num in left:
                if not path or direction_matches(path[-1], num, s[sig_pos]):
                    left.remove(num)
                    path.append(num)
                    if result := dfs(sig_pos + 1, left, path):
                        return result
                    path.pop()
                    left.add(num)

            return None

        if result := dfs(-1, set(range(1, len(s) + 2)), []):
            return result
        else:
            raise RuntimeError("This isn't possible")
