from typing import List, Set, Tuple


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack: List[int] = []
        result: List[List[int]] = []
        candidates.sort()

        def dfs(pos: int, left: int) -> None:
            if left == 0:
                result.append(stack.copy())
                return

            if left < 0:
                return

            if pos == len(candidates):
                return

            repeated = 0

            while pos + 1 < len(candidates) and candidates[pos] == candidates[pos + 1]:
                pos += 1
                repeated += 1

            for times in range(repeated + 1):
                stack.append(candidates[pos])
                dfs(pos + 1, left - candidates[pos] * (times + 1))

            for _ in range(repeated + 1):
                stack.pop()

            dfs(pos + 1, left)

        dfs(0, target)

        return result


class Solution1:
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
                if next_pos > pos and candidates[next_pos] == candidates[next_pos - 1]:
                    continue

                path.append(candidates[next_pos])
                dfs(next_pos + 1, total + candidates[next_pos])
                path.pop()

        dfs(0, 0)

        return [list(r) for r in result]
