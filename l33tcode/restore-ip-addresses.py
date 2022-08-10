from typing import List


class Solution:
    def restoreIpAddresses(self, string: str) -> List[str]:
        result: List[str] = []
        stack: List[str] = []

        def dfs(pos: int, blocks: int) -> None:
            if pos == len(string):
                if blocks == 4:
                    result.append("".join(stack))

                return

            if blocks == 4:
                return

            for next_pos in range(pos + 1, min(len(string) + 1, pos + 4)):
                substring = string[pos:next_pos]

                if 0 <= int(substring) < 256 and not (
                    len(substring) > 1 and substring[0] == "0"
                ):
                    if stack:
                        stack.append(".")
                    stack.append(substring)
                    dfs(next_pos, blocks + 1)
                    stack.pop()
                    if stack:
                        stack.pop()

        dfs(0, 0)

        return result
