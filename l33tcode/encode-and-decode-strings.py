from typing import List


def number_to_str(number: int) -> str:
    base = 256

    result = []

    for _ in range(4):  # length of chunk length field
        result.append(chr(number % base))
        number = number // base

    if number > 0:
        raise RuntimeError("Number is too large")

    return "".join(reversed(result))


def str_to_number(string: str) -> int:
    base = 256
    result = 0
    for char in string:
        result = result * base + ord(char)

    return result


class Codec:
    def encode(self, strs: List[str]) -> str:
        result_list: List[str] = []

        for string in strs:
            result_list.append(number_to_str(len(string)) + string)

        return "".join(result_list)

    def decode(self, s: str) -> List[str]:
        result_list: List[str] = []

        pos = 0

        while pos < len(s):
            chunk_length = str_to_number(s[pos : pos + 4])
            start = pos + 4
            end = start + chunk_length
            result_list.append(s[start : end])

            pos = end

        return result_list


class CodecEscape:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        result_list = []

        for string in strs:
            for char in string:
                if char == "\\":
                    result_list.append(char)
                result_list.append(char)

            result_list.append("\\n")

        return "".join(["".join(r for r in result_list)])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        result_list: List[List[str]] = [[]]

        pos = 0
        while pos < len(s):
            if pos < len(s) - 1 and s[pos] == "\\":
                if s[pos + 1] == "\\":
                    result_list[-1].append("\\")
                elif s[pos + 1] == "n":
                    result_list.append([])

                pos += 1
            else:
                result_list[-1].append(s[pos])

            pos += 1

        if not result_list[-1]:
            result_list.pop()

        return ["".join(r) for r in result_list]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
