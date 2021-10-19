from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    for k in range(j + 1, len(nums2)):
                        if nums2[j] < nums2[k]:
                            ans[i] = nums2[k]
                            break

        return ans
