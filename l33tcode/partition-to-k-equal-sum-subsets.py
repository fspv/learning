from typing import List


class Solution:
    def canPartitionKSubsetsBruteForce(self, nums: List[int], k: int) -> bool:
        capacity = sum(nums) // k
        if capacity != (sum(nums) / k):
            return False

        groups = [sum(nums) // k] * k

        def dfs(nums_pos: int) -> bool:
            if nums_pos == len(nums):
                return groups.count(0) == k

            for groups_pos in range(k):
                if groups[groups_pos] - nums[nums_pos] >= 0:
                    groups[groups_pos] -= nums[nums_pos]
                    if dfs(nums_pos + 1):
                        return True
                    groups[groups_pos] += nums[nums_pos]

                if groups[groups_pos] == capacity:
                    return False

            return False

        return dfs(0)

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        capacity = sum(nums) // k

        used = [False] * len(nums)

        def dfs(
            pos: int, prev_sum: int, used_count: int, buckets: int, start_pos: int
        ) -> bool:
            if buckets > k:
                return False

            if used_count == len(nums):
                return buckets == k

            for next_pos in range(start_pos, len(nums)):
                if not used[next_pos]:
                    used[next_pos] = True
                    if prev_sum + nums[next_pos] < capacity:
                        if dfs(
                            next_pos,
                            prev_sum + nums[next_pos],
                            used_count + 1,
                            buckets,
                            next_pos + 1,
                        ):
                            return True
                    elif prev_sum + nums[next_pos] == capacity:
                        if dfs(next_pos, 0, used_count + 1, buckets + 1, 0):
                            return True
                    used[next_pos] = False

            return False

        return dfs(0, 0, 0, 0, 0)
