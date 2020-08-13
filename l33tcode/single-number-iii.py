class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0  # a ^ b
        for num in nums:
            xor ^= num

        diff = xor & (-xor)

        num1, num2 = 0, 0
        for num in nums:
            if num & diff > 0:
                num1 ^= num
            else:
                num2 ^= num

        return [num1, num2]
