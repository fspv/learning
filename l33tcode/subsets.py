class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub_rec(pos, prev):
            if pos == len(nums):
                return [[]]

            result = [prev]

            for r_pos in range(pos + 1, len(nums)):
                for s in sub_rec(r_pos, prev + [nums[r_pos]]):
                    result.append(s)

            return result

        return sub_rec(-1, [])
