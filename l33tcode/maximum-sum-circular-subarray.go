package main

import (
	"math"
)

func maxSubarraySumCircular(A []int) int {
	total := 0.0
	curMax, curMin := 0.0, 0.0
	overallMax, overallMin := float64(A[0]), 0.0

	for pos, _ := range A {
		num := float64(A[pos])
		total += num
		if num+curMax >= 0 {
			curMax = num+curMax
			overallMax = math.Max(curMax, overallMax)
		} else {
			curMax = 0
			overallMax = math.Max(num, overallMax)
		}
	}

	for pos, _ := range A[:len(A)-1] {
		num := float64(A[pos])
		curMin = math.Min(num+curMin, 0)
		overallMin = math.Min(curMin, overallMin)
	}

	return int(math.Max(overallMax, total-overallMin))
}
