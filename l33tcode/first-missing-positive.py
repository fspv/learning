from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Move all non-positive numbers to the end
        offset = len(nums)

        for pos in range(len(nums)):
            if pos >= offset:
                break

            if nums[pos] <= 0:
                offset -= 1
                nums[pos], nums[offset] = nums[offset], nums[pos]

        # Move all the numbers to positions representing their values
        # if possible
        for pos in range(offset):
            while (
                nums[pos] < offset
                and nums[pos] > 0
                and nums[pos] != pos + 1
                and nums[pos] != nums[nums[pos] - 1]
            ):
                num = nums[pos]
                nums[pos], nums[num - 1] = nums[num - 1], nums[pos]

        # Find a missing element
        missing = 1

        for num in nums:
            if num > 0:
                if num == missing:
                    missing += 1
                else:
                    break

        return missing

    def firstMissingPositiveIncorrectQuickselect(self, nums: List[int]) -> int:
        # Works only if there are none repetitions
        negatives = sum(1 for num in nums if num <= 0)

        left, right = 0, len(nums)

        max_left = 0

        while left < right:
            pivot = nums[right - 1]
            offset = 0

            for pos in range(left, right):
                if nums[pos] <= pivot:
                    max_left = max(max_left, nums[pos])
                    nums[pos], nums[left + offset] = nums[left + offset], nums[pos]
                    offset += 1

            if max_left == left + offset - negatives:
                left = left + offset
            else:
                right = left + offset - 1

        return nums[left] + 1

    def firstMissingPositiveOld(self, nums: List[int]) -> int:
        MAX_BUCKETS_SIZE = 1000

        begin, end = float("+inf"), float("-inf")
        for num in nums:
            if num > 0:
                begin = min(begin, num)
                end = max(end, num)

        # Gap at the beginning, 1 is the only possible answer
        if begin > 1:
            return 1

        while begin < end - 1:
            # Fit all elements into at most MAX_BUCKETS_SIZE buckets
            buckets_count = min((end - begin), MAX_BUCKETS_SIZE) + 1
            bucket_size = (end - begin) // (buckets_count - 1)
            buckets = [0] * buckets_count  # type: ignore

            # Update counts of elements in each bucket
            for num in nums:
                if begin <= num <= end:
                    buckets[(num - begin) // bucket_size] += 1

            # Find the first bucket that has less than bucket_size elements
            for bucket, count in enumerate(buckets):
                if count < bucket_size:
                    # Update begin and end with this bucket to continue search
                    # for the missing element here
                    begin = begin + bucket * bucket_size
                    end = begin + bucket_size

                    # This is an element we're looking for, since we have 0
                    # elements in the bucket of size 1
                    if bucket_size == 1:
                        return begin  # type: ignore

                    break

            # Bucket size is 1 and no gaps found
            if bucket_size == 1:
                break

        # No gaps found, return the element next to the last element
        return end + 1  # type: ignore
