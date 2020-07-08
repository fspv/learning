package main

import (
	"strings"
)

func solveNQueens(n int) [][]string {
	rows, cols := n, n
	rowConstraints := make([]bool, rows)
	colConstraints := make([]bool, cols)
	diagConstraints := make([]bool, rows + cols)
	diagNegConstraints := make([]bool, rows + cols)

	// Generate board
	var genBoard func() [][]string
	genBoard = func() [][]string {
		board := [][]string{}
		for row := range make([]bool, rows) {
			board = append(board, []string{})
			for _ = range make([]bool, cols) {
				board[row] = append(board[row], ".")
			}
		}
		return board
	}
	board := genBoard()

	// Output array
	result := [][]string{}

	checkConstraints := func(row, col int) bool {
		if rowConstraints[row] || colConstraints[col] {
			return false
		}
		if diagConstraints[row + col] || diagNegConstraints[row - col + rows] {
			return false
		}

		return true
	}

	setConstraints := func(row, col int) {
		rowConstraints[row], colConstraints[col] = true, true
		diagConstraints[row + col], diagNegConstraints[row - col + rows] = true, true
	}

	unsetConstraints := func(row, col int) {
		rowConstraints[row], colConstraints[col] = false, false
		diagConstraints[row + col], diagNegConstraints[row - col + rows] = false, false
	}

	var dfs func(row int)
	dfs = func(row int) {
		if row == rows {
			curBoard := []string{}
			for boardRow := range board {
				curBoard = append(curBoard, strings.Join(board[boardRow], ""))
			}
			result = append(result, curBoard)
			return
		}

		for col := range make([]bool, cols) {
			if checkConstraints(row, col) {
				setConstraints(row, col)
				board[row][col] = "Q"
				dfs(row + 1)
				unsetConstraints(row, col)
				board[row][col] = "."
			}
		}
		return
	}

	dfs(0)

	return result
}
