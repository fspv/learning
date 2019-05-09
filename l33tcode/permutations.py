class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        snums = set(nums)

        def dfs():
            if not len(snums):
                return [[]]

            local_result = []

            for num in list(snums):
                snums.remove(num)
                for res in dfs():
                    local_result.append(res + [num])
                snums.add(num)

            return local_result

        return dfs()
