from collections import Counter


class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._counter = Counter()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self._counter[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self._counter:
            diff = value - number
            if diff in self._counter:
                if diff == number:
                    if self._counter[number] > 1:
                        return True
                else:
                    return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
