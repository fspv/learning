class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        counter1 = 0
        counter2 = 0

        for num in nums:
            counter2 ^= (counter1 & num)
            counter1 ^= counter1 ^ num

            mask = ~ (counter1 & counter2)

            counter1 &= mask
            counter2 &= mask

        return counter1
