class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for number in range(1, n + 1):
            string = ""

            if number % 3 == 0:
                string += "Fizz"
            if number % 5 == 0:
                string += "Buzz"

            string = string or str(number)

            result.append(string)

        return result
