package main

func findTargetSumWays(nums []int, S int) int {
	if len(nums) == 0 {
		return 0
	}

	total := 0
	for _, num := range nums {
		total += num
	}

	if (total+S)%2 != 0 {
		return 0
	}

	sumTarget := (total + S) / 2
	dp := map[int]int{0: 1}

	for pos := 0; pos < len(nums); pos++ {
		dp_new := map[int]int{}
		for capacity, count := range dp {
			dp_new[capacity] += count
			if capacity+nums[pos] <= sumTarget {
				dp_new[capacity+nums[pos]] += count
			}
		}
		dp = dp_new
	}

	if _, ok := dp[sumTarget]; !ok {
		return 0
	}

	return dp[sumTarget]
}
