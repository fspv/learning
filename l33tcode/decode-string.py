import unittest
from typing import List, Iterator, Tuple


class Solution:
    def decodeString(self, s: str) -> str:
        result = ""

        stack = []
        pos = 0

        while pos < len(s):
            if s[pos] == "]":
                while stack and s[pos] == "]":
                    last = stack.pop()
                    result_string = last[0] * last[1]
                    if stack:
                        tmp_num, tmp_string = stack.pop()
                        stack.append((tmp_num, tmp_string + result_string))
                    else:
                        result += result_string

                    pos += 1
            elif s[pos].isdigit():
                num_start = pos

                while s[pos] != "[":
                    pos += 1

                num = int(s[num_start:pos])

                pos += 1

                str_start = pos

                while not (s[pos] == "]" or s[pos].isdigit()):
                    pos += 1

                stack.append((num, s[str_start:pos]))
            else:
                result_string = s[pos]
                if stack:
                    tmp_num, tmp_string = stack.pop()
                    stack.append((tmp_num, tmp_string + result_string))
                else:
                    result += result_string
                pos += 1

        return result


def get_repeat(string: str, pos: int) -> Tuple[int, int]:
    start, end = pos, pos
    while string[end].isdigit():
        end += 1

    return end, int(string[start:end])


def dfs(string: str, pos: int) -> Tuple[int, List[str]]:
    result: List[str] = []

    while pos < len(string):
        if string[pos].isdigit():
            pos, repeat = get_repeat(string, pos)
            pos, substrings = dfs(string, pos + 1)

            result.extend(substrings * repeat)
        elif string[pos] == "]":
            pos += 1
            break
        else:
            result.append(string[pos])
            pos += 1

    return pos, result


class Solution2:
    def decodeString(self, s: str) -> str:
        _, substrings = dfs(s, 0)
        return "".join(substrings)


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case1(self):
        self.assertEqual(self.sol.decodeString("3[a]2[bc]"), "aaabcbc")

    def test_case2(self):
        self.assertEqual(self.sol.decodeString("3[a2[c]]"), "accaccacc")

    def test_case3(self):
        self.assertEqual(self.sol.decodeString("2[abc]3[cd]ef"), "abcabccdcdcdef")

    def test_case4(self):
        self.assertEqual(self.sol.decodeString("10[a]"), "aaaaaaaaaa")

    def test_case5(self):
        self.assertEqual(self.sol.decodeString("bx10[a]"), "bxaaaaaaaaaa")

    def test_case6(self):
        self.assertEqual(
            self.sol.decodeString("3[a2[bc4[x1[b]]]]efg"),
            "abcxbxbxbxbbcxbxbxbxbabcxbxbxbxbbcxbxbxbxbabcxbxbxbxbbcxbxbxbxbefg",
        )

    def test_case7(self):
        self.assertEqual(self.sol.decodeString("3[a]2[b4[F]c]"), "aaabFFFFcbFFFFc")


if __name__ == "__main__":
    unittest.main()
