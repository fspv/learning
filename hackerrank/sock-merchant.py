def sockMerchant(n, ar):
    items_with_color = {}

    for i in range(n):
        items_with_color[ar[i]] = items_with_color.get(ar[i], 0) + 1

    result = 0

    for k, v in items_with_color.items():
        result += v // 2

    return result


class TestSockMerchant:
    def test_empty(self):
        assert sockMerchant(0, []) == 0

    def test_one(self):
        assert sockMerchant(1, [1]) == 0

    def test_two1(self):
        assert sockMerchant(2, [1, 2]) == 0

    def test_two1(self):
        assert sockMerchant(2, [2, 2]) == 1

    def test_custom1(self):
        assert sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]) == 3
