MIN, MAX = -(10**6) - 1, 10**6 + 1


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        first = nums2 if len(nums1) >= len(nums2) else nums1
        second = nums1 if len(nums1) >= len(nums2) else nums2

        left, right = 0, len(first)
        median = (len(first) + len(second) + 1) // 2

        while left <= right:
            mid_first = left + (right - left) // 2
            mid_second = median - mid_first

            first_before = first[mid_first - 1] if mid_first > 0 else MIN
            first_after = first[mid_first] if mid_first < len(first) else MAX
            second_before = second[mid_second - 1] if mid_second > 0 else MIN
            second_after = second[mid_second] if mid_second < len(second) else MAX

            if first_before <= second_after and second_before <= first_after:
                if (len(first) + len(second)) % 2 == 0:
                    return (
                        max(first_before, second_before)
                        + min(first_after, second_after)
                    ) / 2.0
                else:
                    return float(max(first_before, second_before))
            elif first_before > second_after:
                right = mid_first - 1
            else:
                left = mid_first + 1

        raise ValueError("Median doesn't exist")
