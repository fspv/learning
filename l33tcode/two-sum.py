class Solution:
    def twoSum(self, nums: list[int], target: int) -> tuple[int, int]:
        num_to_pos = {}
        for i, num in enumerate(nums):
            second = target - num
            if second in num_to_pos:
                return i, num_to_pos[second]

            num_to_pos[num] = i

        raise ValueError("Not found")
