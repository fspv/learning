from typing import List, Dict


class Solution:
    def findErrorNumsRadixSort(self, nums: List[int]) -> List[int]:
        def position_sort(array: List[int], base: int, position: int) -> List[int]:
            result = [0] * len(array)
            buckets = [0] * base

            exp = base ** position

            for num in array:
                buckets[(num // exp) % base] += 1

            for pos in range(1, len(buckets)):
                buckets[pos] += buckets[pos - 1]

            for num in reversed(array):
                result[buckets[(num // exp) % base] - 1] = num
                buckets[(num // exp) % base] -= 1

            return result

        def radix_sort(array: List[int]) -> List[int]:
            max_num = max(array)
            max_position = 0

            while max_num:
                max_num //= 10
                max_position += 1

            for position in range(max_position):
                array = position_sort(array, 10, position)

            return array

        nums.append(len(nums) + 1)
        nums.append(0)
        sorted_nums = radix_sort(nums)

        duplicated, removed = 0, 0

        for pos in range(1, len(sorted_nums)):
            if sorted_nums[pos - 1] == sorted_nums[pos]:
                duplicated = sorted_nums[pos]
            if (sorted_nums[pos] - sorted_nums[pos - 1]) > 1:
                removed = sorted_nums[pos] - 1

        return [duplicated, removed]

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
