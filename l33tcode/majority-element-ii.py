from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = max(nums) + 1, max(nums) + 1
        count1, count2 = 0, 0

        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        result: List[int] = []

        if nums.count(candidate1) > len(nums) // 3:
            result.append(candidate1)

        if nums.count(candidate2) > len(nums) // 3:
            result.append(candidate2)

        return result

    def majorityElementBruteforce(self, nums: List[int]) -> List[int]:
        nums.sort()

        result: List[int] = []

        num = None
        count = 0

        for pos in range(len(nums)):
            if num == nums[pos]:
                count += 1
            else:
                count = 1
                num = nums[pos]

            if count > len(nums) // 3 and (not result or result[-1] != num) and num:
                result.append(num)

        return result
