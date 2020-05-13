package main

func countBattleships(board [][]byte) int {
	count := 0
	for row, _ := range make([]bool, len(board)) {
		for col, _ := range make([]bool, len(board[row])) {
			seen := false
			if row > 0 {
				if board[row-1][col] == 'X' {
					seen = true
				}
			}
			if col > 0 {
				if board[row][col-1] == 'X' {
					seen = true
				}
			}
			if !seen && board[row][col] == 'X'{
				count += 1
			}
		}
	}

	return count
}
