package main

func exist(board [][]byte, word string) bool {
	rows, cols := len(board), len(board[0])
	createVisited := func(rows, cols int) [][]bool {
		result := [][]bool{}

		for row := range make([]bool, rows) {
			result = append(result, []bool{})
			for _ = range make([]bool, cols) {
				result[row] = append(result[row], false)
			}
		}
		return result
	}
	neighbours := func(row, col int, visited *[][]bool) [][]int {
		tmp := [][]int{}
		tmp = append(tmp, []int{row - 1, col})
		tmp = append(tmp, []int{row + 1, col})
		tmp = append(tmp, []int{row, col - 1})
		tmp = append(tmp, []int{row, col + 1})
		result := [][]int{}
		for _, neighbour := range tmp {
			neighRow, neighCol := neighbour[0], neighbour[1]
			if neighRow >= 0 && neighRow < rows && neighCol >= 0 && neighCol < cols {
				if !(*visited)[neighRow][neighCol] {
					result = append(result, []int{neighRow, neighCol})
				}
			}
		}
		return result
	}
	var backtrack func(row, col int, wordPos int, visited *[][]bool) bool
	backtrack = func(row, col int, wordPos int, visited *[][]bool) bool {
		if word[wordPos] != board[row][col] {
			return false
		}

		if wordPos == len(word)-1 {
			return true
		}

		for _, neighbour := range neighbours(row, col, visited) {
			neighRow, neighCol := neighbour[0], neighbour[1]
			(*visited)[row][col] = true
			if backtrack(neighRow, neighCol, wordPos+1, visited) {
				return true
			}
			(*visited)[row][col] = false
		}
		return false
	}

	visited := createVisited(rows, cols)
	for row := range board {
		for col := range board[0] {
			if backtrack(row, col, 0, &visited) {
				return true
			}
		}
	}
	return false
}
