class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

	result = []

        char_index = 0

        while len(result) == char_index:
            for s in strs:
                if len(s) > char_index:
                    if len(result) <= char_index:
                        result.append(s[char_index])
                    else:
                        if s[char_index] != result[char_index]:
                            result.pop()
                            break
                else:
                    if len(result) > char_index:
                        result.pop()
                    break

            char_index += 1

        return ''.join(result)


solution = Solution()

for i in range(1000000):
    assert solution.longestCommonPrefix([""]) == ""
    assert solution.longestCommonPrefix(["a"]) == "a"
    assert solution.longestCommonPrefix(["aa","a"]) == "a"
    assert solution.longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog","racecar","car"]) == ""
