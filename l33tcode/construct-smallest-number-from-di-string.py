class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack: list[int] = []
        seen: set[int] = set()

        def dfs(pos: int) -> bool:
            if pos == len(pattern):
                return True


            for num in range(1, 10):
                if pattern[pos] == "I":
                    if stack[-1] + num < 10:
                        if stack[-1] + num in seen:
                            continue
                        seen.add(stack[-1] + num)
                        stack.append(stack[-1] + num)
                        if dfs(pos + 1):
                            return True
                        stack.pop()
                        seen.discard(stack[-1] + num)
                else:
                    if stack[-1] - num > 0:
                        if stack[-1] - num in seen:
                            continue
                        seen.add(stack[-1] - num)
                        stack.append(stack[-1] - num)
                        if dfs(pos + 1):
                            return True
                        stack.pop()
                        seen.discard(stack[-1] - num)

            return False

        for num in range(1, 10):
            stack.append(num)
            seen.add(num)
            if dfs(0):
                break
            stack.pop()
            seen.discard(num)

        return "".join(map(str, stack))
