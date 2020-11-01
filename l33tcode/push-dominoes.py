class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        output = list(dominoes)

        last_right = -1

        for dominoe in range(len(dominoes)):
            if dominoes[dominoe] == "." and last_right >= 0:
                output[dominoe] = "R"

            if dominoes[dominoe] == "L" and last_right >= 0:
                left_ptr, right_ptr = last_right + 1, dominoe - 1
                while left_ptr < right_ptr:
                    output[left_ptr] = "R"
                    output[right_ptr] = "L"
                    left_ptr += 1
                    right_ptr -= 1

                if left_ptr == right_ptr:
                    output[left_ptr] = "."

                last_right = -1

            if dominoes[dominoe] == "R":
                last_right = dominoe

        last_left = -1

        for dominoe in reversed(range(len(dominoes))):
            if dominoes[dominoe] == "." and last_left >= 0:
                output[dominoe] = "L"

            if dominoes[dominoe] == "R" and last_left >= 0:
                left_ptr, right_ptr = dominoe + 1, last_left - 1
                while left_ptr < right_ptr:
                    output[left_ptr] = "R"
                    output[right_ptr] = "L"
                    left_ptr += 1
                    right_ptr -= 1

                if left_ptr == right_ptr:
                    output[left_ptr] = "."

                last_left = -1

            if dominoes[dominoe] == "L":
                last_left = dominoe

        return "".join(output)
