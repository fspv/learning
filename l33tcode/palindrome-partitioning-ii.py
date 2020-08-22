from typing import List
from collections import defaultdict
from functools import lru_cache


class Solution:
    @staticmethod
    def max_palindromes(string: str) -> List[List[int]]:
        def palindrome_here_odd(pos: int, offset: int) -> int:
            left, right = pos - offset, pos + offset
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1

            return right - pos

        def palindrome_here_even(pos: int, offset: int) -> int:
            left, right = pos - 1 - offset, pos + offset
            while left >= 0 and right < len(string) and string[left] == string[right]:
                left -= 1
                right += 1

            return right - pos

        odd_palindromes: List[int] = []
        rightmost_pos, middle_pos = -1, -1

        for pos in range(len(string)):
            offset = 0

            if pos < rightmost_pos:
                offset = odd_palindromes[middle_pos - (pos - middle_pos)]
                if pos + offset > rightmost_pos:
                    offset = rightmost_pos - pos

            palindrome_len = palindrome_here_odd(pos, offset)
            if pos + palindrome_len > rightmost_pos:
                rightmost_pos = pos + palindrome_len
                middle_pos = pos

            odd_palindromes.append(palindrome_len)

        even_palindromes = [0]
        rightmost_pos, middle_pos = -1, -1

        for pos in range(1, len(string)):
            offset = 0

            if pos < rightmost_pos:
                offset = even_palindromes[middle_pos - (pos - middle_pos)]
                if pos + offset > rightmost_pos:
                    offset = rightmost_pos - pos

            palindrome_len = palindrome_here_even(pos, offset)
            if pos + palindrome_len > rightmost_pos:
                rightmost_pos = pos + palindrome_len
                middle_pos = pos

            even_palindromes.append(palindrome_len)

        return [odd_palindromes, even_palindromes]

    def minCutWrong(self, s: str) -> int:
        if not s:
            return 0
        odd_palindromes, even_palindromes = self.max_palindromes(s)

        # print(s, odd_palindromes, even_palindromes)

        max_jump_odd = [0] * len(s)

        for pos, length in enumerate(odd_palindromes):
            max_jump_odd[pos - (length - 1)] = max(max_jump_odd[pos - (length - 1)], pos + length - 1 + 1)

        max_jump_even = [0] * len(s)
        for pos, length in enumerate(even_palindromes):
            max_jump_even[pos - length] = max(max_jump_even[pos - length], pos + length)

        dp = list(range((len(s) + 1)))

        for pos in range(len(s)):
            left, right = pos, max_jump_even[pos]
            while left < right:
                dp[right] = min(dp[right], dp[left] + 1)
                left += 1
                right -= 1

            left, right = pos, max_jump_odd[pos]
            while left < right:
                dp[right] = min(dp[right], dp[left] + 1)
                left += 1
                right -= 1

        print(dp)
        print(max_jump_odd, max_jump_even)

        return dp[-1] - 1


    def minCut(self, s: str) -> int:
        if not s:
            return 0
        palindrome = [[False] * len(s) for _ in s]

        def check_palindrome(left: int, right: int) -> None:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome[left][right] = True
                left -= 1
                right += 1


        for pos in range(len(s)):
            check_palindrome(pos, pos)
            check_palindrome(pos, pos + 1)


        dp = list(range(len(s) + 1))

        for left in range(len(s)):
            for right in range(left, len(s)):
                if palindrome[left][right]:
                    dp[right + 1] = min(
                        dp[right + 1],
                        dp[left] + 1,
                    )

        return dp[-1] - 1


    def minCutRecursive(self, s: str) -> int:
        if not s:
            return 0
        palindrome = [[False] * len(s) for _ in s]

        def check_palindrome(left: int, right: int) -> None:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                palindrome[left][right] = True
                left -= 1
                right += 1


        for pos in range(len(s)):
            check_palindrome(pos, pos)
            check_palindrome(pos, pos + 1)

        @lru_cache(None)
        def dfs(pos: int) -> int:
            min_lvl = len(s) - pos

            left = pos
            for right in range(left, len(s)):
                if palindrome[left][right]:
                    min_lvl = min(
                        min_lvl,
                        dfs(right + 1) + 1
                    )

            return min_lvl


        return dfs(0) - 1



    def minCutBruteForce(self, s: str) -> int:
        if not s:
            return 0

        mem = defaultdict(list)

        def check_palindrome(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                mem[left].append(right + 1)
                left -= 1
                right += 1

        for pos in range(len(s)):
            check_palindrome(pos, pos)
            check_palindrome(pos, pos + 1)

        def dfs(start, level=0, level_min=float("+inf")):
            if start == len(s) or level == level_min:
                return level

            for start_next in reversed(mem[start]):
                level_min = min(level_min, dfs(start_next, level + 1, level_min))

            return level_min

        return dfs(0) - 1


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_empty(self):
        assert self.sol.minCut("") == 0

    def test_one(self):
        assert self.sol.minCut("a") == 0

    def test_case1(self):
        assert self.sol.minCut("aba") == 0

    def test_case2(self):
        assert self.sol.minCut("aaabaaabaac") == 2

    def test_case3(self):
        assert self.sol.minCut("aab") == 1

    def test_case4(self):
        assert self.sol.minCut("ababababababababababababcbabababababababababababa") == 0

    def test_case5(self):
        assert (
            self.sol.minCut(
                "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
            )
            == 452
        )

    def test_case6(self):
        assert (
            self.sol.minCut(
                "eegiicgaeadbcfacfhifdbiehbgejcaeggcgbahfcajfhjjdgj"
            )
            == 42
        )


    def test_case7(self):
        assert (
            self.sol.minCut(
                "adabdcaebdcebdcacaaaadbbcadabcbeabaadcbcaaddebdbddcbdacdbbaedbdaaecabdceddccbdeeddccdaabbabbdedaaabcdadbdabeacbeadbaddcbaacdbabcccbaceedbcccedbeecbccaecadccbdbdccbcbaacccbddcccbaedbacdbcaccdcaadcbaebebcceabbdcdeaabdbabadeaaaaedbdbcebcbddebccacacddebecabccbbdcbecbaeedcdacdcbdbebbacddddaabaedabbaaabaddcdaadcccdeebcabacdadbaacdccbeceddeebbbdbaaaaabaeecccaebdeabddacbedededebdebabdbcbdcbadbeeceecdcdbbdcbdbeeebcdcabdeeacabdeaedebbcaacdadaecbccbededceceabdcabdeabbcdecdedadcaebaababeedcaacdbdacbccdbcece"
            )
            == 273
        )
