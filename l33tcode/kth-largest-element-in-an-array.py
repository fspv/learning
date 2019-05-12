class Solution:
    def findKthLargest(self, nums, k):
        def quicksearch(left, right):
            pivot = right - 1
            lleft = left

            for pos in range(left, right):
                if nums[pos] >= nums[pivot]:
                    nums[lleft], nums[pos] = nums[pos], nums[lleft]
                    lleft += 1

            if lleft > k:
                return quicksearch(left, lleft - 1)
            elif lleft < k:
                return quicksearch(lleft, right)
            else:
                return nums[lleft - 1]

        return quicksearch(0, len(nums))


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.findKthLargest([1], 1) == 1

    def test_custom1(self):
        assert self.sol.findKthLargest([3,2,1,5,6,4], 2) == 5

    def test_custom2(self):
        assert self.sol.findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
