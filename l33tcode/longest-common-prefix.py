class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        char_index = 0

        while len(strs[0]) > char_index:
            for string in strs:
                if (
                    len(string) == char_index
                    or string[char_index] != strs[0][char_index]
                ):
                    return string[:char_index]

            char_index += 1

        return strs[0][:char_index]


solution = Solution()

for i in range(1000000):
    assert solution.longestCommonPrefix([""]) == ""
    assert solution.longestCommonPrefix(["a"]) == "a"
    assert solution.longestCommonPrefix(["aa", "a"]) == "a"
    assert solution.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert solution.longestCommonPrefix(["dog", "racecar", "car"]) == ""
