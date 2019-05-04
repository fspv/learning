from functools import lru_cache

class Solution:
    def generateParenthesis(self, n):
        result = []
        check = []
        open_left = close_left = n

        @lru_cache(None)
        def find_valid(res_str, open_left, close_left):
            if open_left == 0 and close_left == 0 and len(check) == 0:
                result.append(res_str)

            if open_left > 0:
                res_str += "("
                check.append("(")
                find_valid(res_str, open_left - 1, close_left)
                res_str = res_str[:-1]
                check.pop()

            if check and check[-1] == "(" and close_left > 0:
                res_str += ")"
                check.pop()
                find_valid(res_str, open_left, close_left - 1)
                res_str = res_str[:-1]
                check.append("(")

        find_valid("", n, n)

        return result
