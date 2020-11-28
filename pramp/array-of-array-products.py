def array_of_array_products_old(arr):
    if len(arr) < 2:
        return []

    left_right_prod = []
    right_left_prod = []

    prod = 1
    for num in arr:
        prod *= num
        left_right_prod.append(prod)

    prod = 1
    for num in reversed(arr):
        prod *= num
        right_left_prod.append(prod)

    result = []

    for pos in range(len(arr)):
        left = left_right_prod[pos - 1] if pos > 0 else 1
        right = right_left_prod[len(arr) - (pos + 1) - 1] if pos < len(arr) - 1 else 1
        result.append(left * right)

    return result


def array_of_array_products(arr):
    if len(arr) < 2:
        return []

    def bisect(num, target):
        left, right = 0, target

        while left < right:
            middle = (left + right) // 2

            if num * middle < target:
                left = middle
            elif num * middle > target:
                right = middle
            else:
                return middle

    prod = 1
    for num in arr:
        prod *= num

    result = []
    for num in arr:
        result.append(bisect(num, prod) or num)

    return result
