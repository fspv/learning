class Solution:
    def mergeArrays(
        self, nums1: list[list[int]], nums2: list[list[int]]
    ) -> list[list[int]]:
        ptr1, ptr2 = 0, 0

        result: list[list[int]] = []

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1][0] == nums2[ptr2][0]:
                result.append([nums1[ptr1][0], nums1[ptr1][1] + nums2[ptr2][1]])
                ptr1 += 1
                ptr2 += 1
            elif nums1[ptr1][0] < nums2[ptr2][0]:
                result.append([nums1[ptr1][0], nums1[ptr1][1]])
                ptr1 += 1
            elif nums1[ptr1][0] > nums2[ptr2][0]:
                result.append([nums2[ptr2][0], nums2[ptr2][1]])
                ptr2 += 1

        for ptr in range(ptr1, len(nums1)):
            result.append([nums1[ptr][0], nums1[ptr][1]])

        for ptr in range(ptr2, len(nums2)):
            result.append([nums2[ptr][0], nums2[ptr][1]])

        return result
