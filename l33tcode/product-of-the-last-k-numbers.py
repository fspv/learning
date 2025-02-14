class ProductOfNumbers:
    _prefix_product: list[int]

    def __init__(self) -> None:
        self._prefix_product = [1]

    def add(self, num: int) -> None:
        if num:
            self._prefix_product.append(self._prefix_product[-1] * num)
        else:
            self._prefix_product = [1]

    def getProduct(self, k: int) -> int:
        if len(self._prefix_product) <= k:
            return 0

        return self._prefix_product[-1] // self._prefix_product[-k - 1]
