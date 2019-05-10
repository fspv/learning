class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for f in path.split("/"):
            if f in [".", ""]:
                pass
            elif f == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(f)

        return "/" + "/".join(stack)
