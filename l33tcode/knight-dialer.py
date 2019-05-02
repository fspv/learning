class Solution:
    def knightDialer(self, N):
        moves = {
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
            0: [4, 6],
        }

        counter = [1] * 10

        for _ in range(1, N):
            old_counter = counter
            counter = [0] * 10

            for num in range(10):
                for move in moves[num]:
                    counter[move] += old_counter[num]

        return sum(counter) % (10 ** 9 + 7)


class TestSolution:
    def setup(self):
        self.sol = Solution()

    def test_one(self):
        assert self.sol.knightDialer(1) == 10

    def test_two(self):
        assert self.sol.knightDialer(2) == 20

    def test_three(self):
        assert self.sol.knightDialer(3) == 46

    def test_four(self):
        assert self.sol.knightDialer(4) == 104

    def test_161(self):
        assert self.sol.knightDialer(161) == 533302150

    def test_5000(self):
        assert self.sol.knightDialer(5000) == 406880451
