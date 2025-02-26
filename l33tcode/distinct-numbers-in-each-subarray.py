from collections import Counter


class Solution:
    def distinctNumbers(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums[:k])

        result: list[int] = []

        for pos in range(len(nums) - k + 1):
            result.append(len(counter))

            if counter[nums[pos]] > 0:
                counter[nums[pos]] -= 1
            if counter[nums[pos]] == 0:
                del counter[nums[pos]]

            if pos + k < len(nums):
                counter[nums[pos + k]] += 1

        return result
