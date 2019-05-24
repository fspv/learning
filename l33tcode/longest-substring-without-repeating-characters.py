class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        str_hash_map = {}
        longest_substr = 0
        left = 0
        right = 0

        for n, c in enumerate(s):
            if c in str_hash_map:
                left = max(str_hash_map[c] + 1, left)

            str_hash_map[c] = n

            right = n

            longest_substr = max(longest_substr, right - left + 1)

        return longest_substr
