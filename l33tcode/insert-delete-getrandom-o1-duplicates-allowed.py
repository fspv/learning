import random
from collections import defaultdict


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = defaultdict(lambda: [])
        self.array = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        self.dict[val].append(len(self.array))
        self.array.append(val)
        return len(self.dict[val]) <= 1

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.dict[val]:
            last = self.array.pop()
            if self.dict[val][-1] != len(self.array):
                self.array[self.dict[val][-1]] = last
                self.dict[last][-1] = self.dict[val][-1]
                self.dict[last].sort()
            self.dict[val].pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.array[random.randint(0, len(self.array) - 1)] if self.array else False


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
