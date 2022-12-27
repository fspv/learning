package main

import "sort"

func maximumBags(capacity []int, rocks []int, additionalRocks int) int {
	missing := make([]int, len(capacity))

	for pos := range capacity {
		missing[pos] = capacity[pos] - rocks[pos]
	}

	sort.Ints(missing)

	result := 0

	for pos := range missing {
		if missing[pos] <= additionalRocks {
			result += 1
			additionalRocks -= missing[pos]
		}
	}

	return result
}
