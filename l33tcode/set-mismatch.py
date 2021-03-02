from typing import List, Dict


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # X is A^B where A and B are numbers we're looking for
        X = 0

        for num in nums:
            X ^= num

        for num in range(len(nums) + 1):
            X ^= num

        # S is A-B
        S = sum(nums) - sum(range(len(nums) + 1))

        # Now we got B = A - S => X ^ A = B = A - S
        # so we just need to find A where above equation holds

        candidates: Dict[int, int] = {}
        for num in nums:
            if X != num and X ^ num == num - S:
                candidates.setdefault(num, 0)
                candidates.setdefault(X ^ num, 0)
                candidates[num] += 1
                candidates[X ^ num] += 1

                if candidates[num] > 1 or candidates[X ^ num] > 1:
                    return [num, X ^ num]

        raise ValueError("Input is incorrect")
