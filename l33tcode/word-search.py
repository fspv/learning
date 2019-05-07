class Solution:
    def exist(self, board, word):
        if not board or not word:
            return False

        visited = [[False for _ in board[0]] for _ in board]
        def find(row, col, pos):
            if pos == len(word) - 1:
                return True

            visited[row][col] = True
            result = False

            for new_row, new_col in [
                (row - 1, col),
                (row, col - 1),
                (row + 1, col),
                (row, col + 1),
            ]:
                if 0 <= new_row < len(board) and \
                   0 <= new_col < len(board[0]) and \
                   board[new_row][new_col] == word[pos + 1] and \
                   not visited[new_row][new_col] and \
                   find(new_row, new_col, pos + 1):
                    result = True
                    break

            visited[row][col] = False
            return result

        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == word[0] and find(row, col, 0):
                    return True

        return False
