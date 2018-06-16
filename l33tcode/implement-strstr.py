class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        haystack_length = len(haystack)

        needle_length = len(needle)
        needle_shift = 0

        haystack_pos = 0

        if needle_length > 0:
            while haystack_pos < haystack_length:
                if haystack[haystack_pos] == needle[needle_shift]:
                    needle_shift += 1
                    haystack_pos += 1
                    if needle_shift == needle_length:
                        return haystack_pos - needle_length
                else:
                    haystack_pos -= needle_shift - 1
                    needle_shift = 0
        else:
            return 0

        return -1


solution = Solution()

assert solution.strStr(haystack="", needle="") == 0
assert solution.strStr(haystack="", needle="ll") == -1
assert solution.strStr(haystack="tset", needle="") == 0
assert solution.strStr(haystack="ll", needle="ll") == 0
assert solution.strStr(haystack="llll", needle="ll") == 0
assert solution.strStr(haystack="hello", needle="ll") == 2
assert solution.strStr(haystack="aaaaa", needle="bba") == -1
assert solution.strStr(haystack="hell", needle="ll") == 2
assert solution.strStr(haystack="helloll", needle="ll") == 2
assert solution.strStr(haystack="mississippi", needle="issip") == 4
