class BrowserHistory:

    def __init__(self, homepage: str):
        self._stack = [homepage]
        self._to_delete = 0

    def visit(self, url: str) -> None:
        for _ in range(self._to_delete):
            self._stack.pop()

        self._to_delete = 0

        self._stack.append(url)

    def back(self, steps: int) -> str:
        self._to_delete += steps
        self._to_delete = min(len(self._stack) - 1, self._to_delete)

        return self._stack[-self._to_delete - 1]

    def forward(self, steps: int) -> str:
        self._to_delete -= steps
        self._to_delete = max(0, self._to_delete)

        return self._stack[-self._to_delete - 1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
