class Solution:
    def isHappy(self, n: int) -> bool:
        def next_num(num):
            return sum(int(i) ** 2 for i in str(num))

        left, right = n, next_num(next_num(n))
        while left != 1:
            if left == right:
                return False

            left, right = next_num(left), next_num(next_num(right))

        return True

    def isHappyStraightforward(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = sum(int(i) ** 2 for i in str(n))

        return True


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_case1(self):
        assert self.sol.isHappy(19)

    def test_case2(self):
        assert not self.sol.isHappy(2)
