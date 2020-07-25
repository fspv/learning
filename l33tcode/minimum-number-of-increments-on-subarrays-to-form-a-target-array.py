class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        prev = 0
        result = 0

        for num in target:
            if num > prev:
                result += (num - prev)
            prev = num

        return result
