from typing import List


class NumberStr:
    def __init__(self, num: int) -> None:
        self.num = num
        self.num_str = str(num)

    def __lt__(self, other: "NumberStr") -> bool:
        return self.num_str + other.num_str < other.num_str + self.num_str

    def __eq__(self, other: "NumberStr") -> bool:
        return self.num_str + other.num_str == other.num_str + self.num_str

    def __str__(self) -> str:
        return "".join(map(str, self.num_str))


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        result = "".join(map(str, sorted(map(NumberStr, nums), reverse=True)))
        if set(result) == {"0"}:
            return "0"

        return result
