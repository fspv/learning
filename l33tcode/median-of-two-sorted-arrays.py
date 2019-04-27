class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        first = nums2 if len(nums1) >= len(nums2) else nums1
        second = nums1 if len(nums1) >= len(nums2) else nums2

        left, right = 0, len(first)
        elem_middle = elem_middle = (len(first) + len(second) + 1) // 2

        while left <= right:
            mid = (left + right) // 2
            split_second = elem_middle - mid
            first_before = first[mid - 1] if mid > 0 else float("-inf")
            first_after = first[mid] if mid < len(first) else float("+inf")
            second_before = second[split_second - 1] if split_second > 0 else float("-inf")
            second_after = second[split_second] if split_second < len(second) else float("+inf")

            if first_before <= second_after and second_before <= first_after:
                if (len(first) + len(second)) % 2 == 0:
                    return (max(first_before, second_before) + min(first_after, second_after)) / 2.0
                else:
                    return float(max(first_before, second_before))
            elif first_before > second_after:
                right = mid - 1
            else:
                left = mid + 1
