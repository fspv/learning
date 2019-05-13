import heapq

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        heap = []

        for pos in range(len(nums1)):
            heapq.heappush(heap, (nums1[pos] + nums2[0], pos, 0))

        result = []

        for pos in range(min(k, len(nums1) * len(nums2))):
            _, pos1, pos2 = heapq.heappop(heap)
            result.append([nums1[pos1], nums2[pos2]])

            if pos2 + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[pos1] + nums2[pos2 + 1], pos1, pos2 + 1),
                )

        return result
