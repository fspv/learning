class Solution:
    def count_and_say_recursion(self, n):
        if n == 1:
            return "1"
        else:
            prev_number = self.count_and_say_recursion(n - 1)
            result = []
            prev_symbol = None
            repeat_counter = 0

            for symbol in prev_number:
                if symbol == prev_symbol:
                    repeat_counter += 1
                    result[-1] = str(repeat_counter) + symbol
                else:
                    repeat_counter = 1
                    result.append(str(repeat_counter) + symbol)
                prev_symbol = symbol
            return ''.join(result)

    def countAndSay(self, n: int) -> str:
        result = ["1", ""]

        for _ in range(n - 1):
            tmp: list[str] = []

            prev, reps = "", 0

            for char in result:
                if char == prev:
                    reps += 1
                else:
                    if reps > 0:
                        tmp.extend([str(reps), prev])
                    prev = char
                    reps = 1

            tmp.append("")

            result = tmp


        return "".join(result)




solution = Solution()

assert solution.countAndSay(1) == "1"
assert solution.countAndSay(2) == "11"
assert solution.countAndSay(3) == "21"
assert solution.countAndSay(4) == "1211"
assert solution.countAndSay(5) == "111221"
