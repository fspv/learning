package main

import (
	"math"
)

func minCost(costs [][]int) int {
	if len(costs) == 0 {
		return 0
	}

	houses := len(costs)
	colors := len(costs[0])
	for pos := range make([]int, houses) {
		if pos != 0 {
			for colorCur := range make([]int, colors) {
				curCost := costs[pos][colorCur]
				costs[pos][colorCur] = math.MaxInt64
				for colorPrev := range make([]int, colors) {
					if colorCur != colorPrev {
						costs[pos][colorCur] = int(math.Min(float64(costs[pos][colorCur]), float64(curCost+costs[pos-1][colorPrev])))
					}
				}
			}
		}
	}

	return int(math.Min(math.Min(float64(costs[houses-1][0]), float64(costs[houses-1][1])), float64(costs[houses-1][2])))
}
