import unittest

# TODO: It is a working solution, but definitely not the best.
# Should improve algorithm to work faster. Have to practice on
# greedy algorithms building.

class Solution:
    def play_face_up(self):
        min_token = None

        for token in self.left_tokens:
            if (min_token is None or self.tokens[token] < self.tokens[min_token]) \
               and self.tokens[token] <= self.P:
                min_token = token

        if min_token is None:
            return False
        else:
            self.P -= self.tokens[min_token]
            self.points += 1
            self.left_tokens.remove(min_token)
            return True

    def play_face_down(self):
        max_token = None

        for token in self.left_tokens:
            if (max_token is None or self.tokens[token] > self.tokens[max_token]):
                max_token = token

        self.P += self.tokens[max_token]
        self.points -= 1
        self.left_tokens.remove(max_token)

    def bagOfTokensScore(self, tokens, P):
        self.points = 0
        self.left_tokens = set()
        self.tokens = tokens
        self.P = P
        self.max_points = 0

        for token in range(len(tokens)):
            self.left_tokens.add(token)

        while len(self.left_tokens):
            if self.points + len(self.left_tokens) < self.max_points:
                break

            if self.points == 0:
                if not self.play_face_up():
                    break
                self.max_points = self.points if self.max_points < self.points else self.max_points
            else:
                if not self.play_face_up():
                    if self.points == 0:
                        break
                    else:
                        self.play_face_down()
                self.max_points = self.points if self.max_points < self.points else self.max_points

        return self.max_points


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test(self):
        self.assertEqual(self.sol.bagOfTokensScore([100], 50), 0)
        self.assertEqual(self.sol.bagOfTokensScore([100, 200], 150), 1)
        self.assertEqual(self.sol.bagOfTokensScore([100, 200, 300, 400], 200), 2)
        self.assertEqual(self.sol.bagOfTokensScore([87, 24, 32], 87), 2)


if __name__ == "__main__":
    unittest.main()
