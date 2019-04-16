class Solution:
    def number_of_tabs(self, string):
        result = 0
        for pos in range(len(string)):
            if string[pos] == "\t":
                result += 1
            else:
                break

        return result

    def lengthLongestPath(self, input: str) -> int:
        stack = [(0, 0)]
        max_len = 0

        for line in input.split("\n"):
            ind_lvl = self.number_of_tabs(line)

            while stack and ind_lvl <= stack[-1][0]:
                stack.pop()

            stack.append(
                (
                    ind_lvl,
                    len(line.rsplit("\t", 1)[-1]) + (stack[-1][1] if stack else 0)
                )
            )
            if "." in line:
                max_len =  max(max_len, stack[-1][1] + len(stack) - 1)

        return max_len
