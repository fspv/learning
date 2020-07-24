package main

func numTrees(n int) int {
	dp := make([]int, n+1)
	dp[0] = 1

	for num := range make([]int, n) {
		elements := num + 1
		for split := range make([]int, elements) {
			dp[elements] += dp[split] * dp[elements-split-1]
		}
	}

	return dp[n]
}
