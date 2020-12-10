class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False

        up = True

        for pos in range(1, len(arr)):
            if arr[pos - 1] < arr[pos]:
                if not up:
                    return False
            elif arr[pos - 1] > arr[pos]:
                if up:
                    up = False
            else:
                return False

        return arr[0] < arr[1] and arr[-2] > arr[-1]
