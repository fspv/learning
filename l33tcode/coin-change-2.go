package main

func change(amount int, coins []int) int {
	dp := [][]int{}
	dp = append(dp, make([]int, amount+1))
	dp[0][0] = 1
	for pos, _ := range coins {
		dp = append(dp, make([]int, amount+1))
		dp[pos+1][0] = 1
	}

	for coin_pos, coin := range coins {
		for amount_pos, _ := range make([]int, amount) {
			dp[coin_pos+1][amount_pos+1] = dp[coin_pos][amount_pos+1]
			if amount_pos+1-coin >= 0 {
				dp[coin_pos+1][amount_pos+1] += dp[coin_pos+1][amount_pos+1-coin]
			}
		}
	}

	return dp[len(coins)][amount]
}
