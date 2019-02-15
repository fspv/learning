class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: 'int') -> 'None':
        self._stack.append(x)
        if len(self._min_stack):
            if x <= self._min_stack[-1]:
                self._min_stack.append(x)
        else:
            self._min_stack.append(x)

    def pop(self) -> 'None':
        top = self._stack.pop()
        if top == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> 'int':
        return self._stack[-1]

    def getMin(self) -> 'int':
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
