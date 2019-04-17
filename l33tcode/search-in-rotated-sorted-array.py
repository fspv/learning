class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] >= nums[0]:
                left = mid + 1
            else:
                right = mid - 1

        pivot = max(left, right)

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            real_mid = (mid + pivot) % len(nums)

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
