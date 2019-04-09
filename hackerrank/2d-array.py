def hourglassSum(arr):
    result = float("-inf")
    for x in range(len(arr) - 2):
        for y in range(len(arr) - 2):
            result = max(
                result,
                sum(
                    [
                        arr[y][x],
                        arr[y][x + 1],
                        arr[y][x + 2],
                        arr[y + 2][x],
                        arr[y + 2][x + 1],
                        arr[y + 2][x + 2],
                        arr[y + 1][x + 1],
                    ]
                ),
            )

    return result
