from typing import List, Tuple


class Parser:
    def __init__(self, string: str) -> None:
        self._input = string

    def _parse_options(self, pos: int) -> Tuple[int, List[str]]:
        result = []

        pos += 1

        while self._input[pos] != "}":
            if self._input[pos] != ",":
                result.append(self._input[pos])

            pos += 1

        return pos + 1, result

    def _parse_char(self, pos: int) -> Tuple[int, List[str]]:
        return pos + 1, [self._input[pos]]

    def parse(self) -> List[List[str]]:
        pos = 0

        result = []

        while pos < len(self._input):
            if self._input[pos] == "{":
                pos, chars = self._parse_options(pos)
                result.append(chars)
            else:
                pos, chars = self._parse_char(pos)
                result.append(chars)

        return result


class Solution:
    def expand(self, S: str) -> List[str]:
        def parse_input(string: str) -> List[List[str]]:
            parser = Parser(string)

            return parser.parse()

        parsed_input = parse_input(S)
        result = []

        def dfs(pos: int, path: List[str]) -> None:
            if pos == len(parsed_input):
                result.append("".join(path))
                return

            for char in sorted(parsed_input[pos]):
                path.append(char)
                dfs(pos + 1, path)
                path.pop()

        dfs(0, [])

        return result
