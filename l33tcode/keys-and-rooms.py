import unittest


class Solution:
    def canVisitAllRooms(self, rooms):
        stack = [0]
        rooms_state = [False] * len(rooms)

        while stack:
            key = stack.pop()
            rooms_state[key] = True

            for new_key in rooms[key]:
                if not rooms_state[new_key]:
                    stack.append(new_key)

        return False not in rooms_state


class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_one_room_empty(self):
        self.assertTrue(self.sol.canVisitAllRooms([[]]))

    def test_one_room(self):
        self.assertTrue(self.sol.canVisitAllRooms([[0]]))

    def test_custom1(self):
        self.assertTrue(self.sol.canVisitAllRooms([[1],[2],[3],[]]))

    def test_custom2(self):
        self.assertFalse(self.sol.canVisitAllRooms([[1,3],[3,0,1],[2],[0]]))


if __name__ == "__main__":
    unittest.main()
