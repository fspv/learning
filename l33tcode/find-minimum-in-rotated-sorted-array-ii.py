class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] < nums[right]:
                right = middle
            elif nums[middle] > nums[right]:
                left = middle + 1
            else:
                right -= 1

        return nums[left]

    def findMinRecursive(self, nums: List[int]) -> int:
        def bisect(left, right):
            if left >= right:
                return nums[left]

            result = float("+inf")
            middle = (left + right) // 2

            if nums[middle] < nums[right]:
                result = min(
                    result, nums[middle], bisect(left, middle - 1)
                )
            elif nums[middle] > nums[right]:
                result = min(
                    result, nums[middle], nums[middle + 1], bisect(middle + 1, right)
                )
            else:
                result = min(
                    result, nums[middle], nums[middle - 1], bisect(left, right - 1)
                )

            return result

        return bisect(0, len(nums) - 1)
