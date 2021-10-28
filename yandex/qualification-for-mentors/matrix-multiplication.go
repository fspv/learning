package main

import "fmt"
import "math"

type Matrix struct {
	n int
	m int
}

func optimalParenthesesTopDown(matrices []Matrix) int {
	dp := [][]int{}

	for pos, _ := range matrices {
		dp = append(dp, make([]int, len(matrices)))
		for rowPos, _ := range dp[pos] {
			dp[pos][rowPos] = math.MaxInt64 // assuming there is no int overflow
		}
		dp[pos][pos] = 0
	}

	for left := len(matrices) - 1; left >= 0; left-- {
		for right := left; right < len(matrices); right++ {
			for middle := left; middle < right; middle++ {
				ops_left := dp[left][middle]
				ops_right := dp[middle+1][right]

				ops := ops_left + ops_right + matrices[left].n*matrices[middle].m*matrices[right].m

				if ops < dp[left][right] {
					dp[left][right] = ops
				}
			}
		}
	}

	return dp[0][len(matrices)-1]
}

func getNumberOfMatrices() int {
	var numMatrices int

	fmt.Scanf("%d", &numMatrices)

	return numMatrices
}

func getMatrix() Matrix {
	var n, m int

	fmt.Scanf("%d %d", &n, &m)

	return Matrix{n, m}
}

func main() {
	numMatrices := getNumberOfMatrices()

	matrices := []Matrix{}

	for pos := 0; pos < numMatrices; pos++ {
		matrices = append(matrices, getMatrix())
	}

	fmt.Println(optimalParenthesesTopDown(matrices))
}
