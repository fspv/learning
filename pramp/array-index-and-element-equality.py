def index_equals_value_search(arr):
  left, right = 0, len(arr) - 1
  result = -1

  while left <= right:
    middle = (left + right) // 2
    if middle > arr[middle]:
      left = middle + 1
    elif middle < arr[middle]:
      right = middle - 1
    else:
      right = middle - 1
      result = middle

  return result
