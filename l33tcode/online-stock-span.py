class StockSpanner:
    def __init__(self):
        self._stack = []

    def next(self, price: int) -> int:
        weight = 1

        while self._stack and self._stack[-1][0] <= price:
            weight += self._stack.pop()[1]

        self._stack.append((price, weight))

        return weight


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
