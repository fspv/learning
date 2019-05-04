class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighs = [[0 for _ in board[0]] for _ in board]

        def count_neighs(row, col, board):
            count = 0
            if row > 0:
                count += board[row - 1][col]
                if col > 0:
                    count += board[row - 1][col - 1]
                if col < len(board[0]) - 1:
                    count += board[row - 1][col + 1]
            if row < len(board) - 1:
                count += board[row + 1][col]
                if col > 0:
                    count += board[row + 1][col - 1]
                if col < len(board[0]) - 1:
                    count += board[row + 1][col + 1]
            if col > 0:
                count += board[row][col - 1]
            if col < len(board[0]) - 1:
                count += board[row][col + 1]

            return count

        for row in range(len(board)):
            for col in range(len(board[0])):
                neighs[row][col] = count_neighs(row, col, board)

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 1:
                    if neighs[row][col] < 2:
                        board[row][col] = 0
                    elif neighs[row][col] > 3:
                        board[row][col] = 0
                else:
                    if neighs[row][col] == 3:
                        board[row][col] = 1
