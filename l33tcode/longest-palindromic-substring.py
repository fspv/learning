class Solution:
    def check_palindrome(self, s: str, left_pointer: int, right_pointer: int) -> str:
        result = ""

        while right_pointer < len(s) and left_pointer >= 0:
            if s[left_pointer] == s[right_pointer]:
                palindrome = s[left_pointer : (right_pointer + 1)]
                result = palindrome if len(palindrome) > len(result) else result
                left_pointer -= 1
                right_pointer += 1
            else:
                break

        return result

    def longestPalindrome(self, s: str) -> str:
        result = ""

        for position in range(len(s)):
            palindrome_type1 = self.check_palindrome(s, position, position)
            result = palindrome_type1 if len(palindrome_type1) > len(result) else result
            palindrome_type2 = self.check_palindrome(s, position - 1, position)
            result = palindrome_type2 if len(palindrome_type2) > len(result) else result

        return result


s = Solution()

assert s.longestPalindrome("cbbd") == "bb"
assert s.longestPalindrome("babad") == "bab" or s.longestPalindrome("babad") == "aba"
assert s.longestPalindrome("bbccbbbbbabbbbb") == "bbbbbabbbbb"
assert s.longestPalindrome("") == ""
assert s.longestPalindrome("a") == "a"
assert s.longestPalindrome("ac") == "a"
assert s.longestPalindrome("ccc") == "ccc"
assert s.longestPalindrome("cccc") == "cccc"
