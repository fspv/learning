def merge(left, right):
    result = []
    count = 0

    left_pos, right_pos = 0, 0
    left_len, right_len = len(left), len(right)

    while left_pos < left_len and right_pos < right_len:
        if left[left_pos] <= right[right_pos]:
            result.append(left[left_pos])
            left_pos += 1
        else:
            result.append(right[right_pos])
            right_pos += 1
            count += left_len - left_pos

    result += left[left_pos:]
    result += right[right_pos:]

    return result, count


def countInversionsRecursive(arr, start, end):
    if end - start < 2:
        return [arr[start]], 0

    middle = (end + start) // 2

    left, left_count = countInversionsRecursive(arr, start, middle)
    right, right_count = countInversionsRecursive(arr, middle, end)

    merged, merged_count = merge(left, right)

    return merged, left_count + right_count + merged_count


def countInversions(arr):
    merged, count = countInversionsRecursive(arr, 0, len(arr))

    return count


class TestMergeSort:
    def test_custom1(self):
        assert countInversionsRecursive([2, 1, 3, 1, 2], 0, 5) == ([1, 1, 2, 2, 3], 5)
