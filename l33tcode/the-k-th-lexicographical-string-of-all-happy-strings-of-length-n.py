class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        result: list[str] = []

        def dfs(pos: int, prev: str) -> bool:
            if pos == n:
                nonlocal count

                count += 1
                return count == k

            for char in ("a", "b", "c"):
                if char != prev:
                    result.append(char)
                    if dfs(pos + 1, char):
                        return True
                    result.pop()

            return False

        dfs(0, "")

        return "".join(result)
