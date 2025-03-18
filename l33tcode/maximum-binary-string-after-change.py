class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        array = [0] * len(binary)
        ones = binary.count("1")
        if ones == len(binary):
            return binary

        for pos in range(len(array)):
            if binary[pos] == "1":
                ones -= 1
            else:
                break

        for pos in range(ones):
            array[-pos - 1] = 1

        for pos in range(len(array) - ones - 1):
            array[pos] = 1

        return "".join(map(str, array))
