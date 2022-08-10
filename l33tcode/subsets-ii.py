from typing import List, Set, Tuple


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        stack: List[int] = []
        result: List[List[int]] = []

        def dfs(pos: int) -> None:
            if pos == len(nums):
                result.append(stack.copy())
                return

            dfs(pos + 1)

            start = pos

            while pos + 1 < len(nums) and nums[pos] == nums[pos + 1]:
                stack.append(nums[pos])
                pos += 1

            stack.append(nums[pos])

            dfs(pos + 1)

            for _ in range(pos - start + 1):
                stack.pop()

        dfs(0)

        return result

    def subsetsWithDupBruteforce(self, nums: List[int]) -> List[List[int]]:
        stack: List[int] = []
        result: List[List[int]] = []

        seen: Set[Tuple[int, ...]] = set()

        def dfs(pos: int) -> None:
            if pos == len(nums):
                if tuple(sorted(stack)) not in seen:
                    result.append(stack.copy())
                    seen.add(tuple(sorted(stack)))

                return

            dfs(pos + 1)

            stack.append(nums[pos])
            dfs(pos + 1)
            stack.pop()

        dfs(0)

        return result
