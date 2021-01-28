from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        result_list = [0] * n
        k -= n

        for pos in reversed(range(n)):
            num = min(k, 25)
            k -= num
            result_list[pos] += num

        return "".join(map(lambda x: chr(ord("a") + x), result_list))

    def getSmallestStringBruteForce(self, n: int, k: int) -> str:
        path: List[str] = []
        result = ""

        def backtrack(pos: int, total: int) -> bool:
            nonlocal result

            if total == k:
                result = "".join(map(lambda x: chr(ord("a") + x - 1), path))
                return True

            if pos == n:
                return False

            if total + (n - pos) * 26 < k:
                return False

            for char in range(1, 27):
                path.append(char)
                if backtrack(pos + 1, total + char):
                    return True
                path.pop()

            return False

        backtrack(0, 0)

        return result
