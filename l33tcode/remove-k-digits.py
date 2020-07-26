from functools import lru_cache


class Solution:
    def removeKdigitsRecursive(self, num: str, k: int) -> str:
        @lru_cache(None)
        def backtrack(removed: int, pos: int) -> int:
            if removed == k and pos == len(num):
                return 0

            min_num = float("+inf")
            left_to_remove = k - removed

            for next_pos in range(pos + 1, min(len(num) + 1, pos + left_to_remove + 2)):
                to_remove = next_pos - pos - 1
                numbers_left = len(num) - pos - 1
                level = numbers_left - left_to_remove

                next_num = backtrack(removed + to_remove, next_pos)
                if pos >= 0:
                    cur_num = int(num[pos]) * 10 ** level + next_num
                else:
                    cur_num = next_num
                if cur_num < min_num:
                    min_num = cur_num

            return min_num

        return str(backtrack(0, -1))

    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        removed = 0
        skipped = 0

        for digit in map(int, num):
            while removed < k and stack and stack[-1] > digit:
                stack.pop()
                removed += 1

            if stack:
                stack.append(digit)
            elif digit != 0:
                stack.append(digit)
            else:
                skipped += 1

        for _ in range(k - removed - skipped):
            stack.pop()

        return "".join(map(str, stack)) or "0"
