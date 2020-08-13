from functools import lru_cache


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = [set() for _ in stones]
        dp[0].add(0)

        stone_pos = {stone: pos for pos, stone in enumerate(stones)}

        for stone in range(len(stones)):
            for jump in dp[stone]:
                for next_jump in filter(
                    lambda j: j > 0, (jump - 1, jump, jump + 1)
                ):
                    next_stone = stones[stone] + next_jump
                    if next_stone in stone_pos:
                        dp[stone_pos[next_stone]].add(next_jump)

            if dp[-1]:
                return True

        return False

    def canCrossRecursive(self, stones: List[int]) -> bool:
        stone_pos = {stone: pos for pos, stone in enumerate(stones)}

        @lru_cache(None)
        def dfs(stone: int, jump: int) -> bool:
            if stone + 1 == len(stones):
                return True

            for next_jump in (jump - 1, jump, jump + 1):
                if next_jump > 0:
                    next_stone = stones[stone] + next_jump
                    if next_stone in stone_pos:
                        if dfs(stone_pos[next_stone], next_jump):
                            return True

            return False

        return dfs(0, 0)
