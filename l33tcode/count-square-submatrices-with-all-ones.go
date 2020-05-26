package main

func countSquares(matrix [][]int) int {
	dp := [][]int{}

	result := 0

	for row, _ := range matrix {
		dp = append(dp, []int{})
		for col, _ := range matrix[row] {
			if matrix[row][col] == 1 {
				minSquareAround := 1000
				if row == 0 || col == 0 {
					minSquareAround = 0
				} else {
					if dp[row][col-1] < minSquareAround {
						minSquareAround = dp[row][col-1]
					}
					if dp[row-1][col] < minSquareAround {
						minSquareAround = dp[row-1][col]
					}
					if dp[row-1][col-1] < minSquareAround {
						minSquareAround = dp[row-1][col-1]
					}
				}
				dp[row] = append(dp[row], minSquareAround+1)
				result += minSquareAround + 1
			} else {
				dp[row] = append(dp[row], 0)
			}
		}
	}

	return result
}
