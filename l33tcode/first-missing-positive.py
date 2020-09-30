from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
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
            buckets = [0] * buckets_count

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
                        return begin

                    break

            # Bucket size is 1 and no gaps found
            if bucket_size == 1:
                break

        # No gaps found, return the element next to the last element
        return end + 1
