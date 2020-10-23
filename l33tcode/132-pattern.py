class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []

        min_before = []

        for pos in range(len(nums)):
            if min_before:
                min_before.append(min(min_before[-1], nums[pos]))
            else:
                min_before.append(nums[pos])

        for pos in reversed(range(len(nums))):
            if nums[pos] > min_before[pos]:
                while stack and stack[-1] <= min_before[pos]:
                    stack.pop()

                if stack and stack[-1] < nums[pos]:
                    return True

                stack.append(nums[pos])

        return False
