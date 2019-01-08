class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        x = nums
        search = target

        found = -1
        p = 0
        r = len(x) - 1

        while found == -1 and r >= p:
            q = int((p + r) / 2)
            if x[q] == search:
                found = q
            if x[q] < search:
                p = q + 1
            elif x[q] > search:
                r = q - 1

        return found

# TODO: write tests
# TODO: speed it up
