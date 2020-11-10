from typing import List, Set, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path: List[int] = []
        result: Set[Tuple[int, ...]] = set()

        if sum(candidates) < target:
            return []

        candidates.sort()

        def dfs(pos: int, total: int) -> None:
            if total == target:
                result.add(tuple(path))

            if pos == len(candidates):
                return

            if total >= target:
                return

            for next_pos in range(pos, len(candidates)):
                if (
                    next_pos > pos
                    and candidates[next_pos] == candidates[next_pos - 1]
                ):
                    continue

                path.append(candidates[next_pos])
                dfs(next_pos + 1, total + candidates[next_pos])
                path.pop()

        dfs(0, 0)

        return [list(r) for r in result]
