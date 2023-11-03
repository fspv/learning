from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        ops = []

        target_pos = 0

        for num in range(1, n + 1):
            if target_pos == len(target):
                break

            stack.append(num)
            ops.append("Push")

            if stack[-1] != target[target_pos]:
                stack.pop()
                ops.append("Pop")
            else:
                target_pos += 1

        return ops
