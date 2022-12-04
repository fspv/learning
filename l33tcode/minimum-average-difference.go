package main

import "math"

func minimumAverageDifference(nums []int) int {
	totalLeft, totalRight := 0.0, 0.0

	for _, num := range nums {
		totalRight += float64(num)
	}

	minAverageDifference := totalRight
	minAverageDifferenceIndex := 0

	for pos, _ := range nums {
		totalLeft += float64(nums[pos])
		totalRight -= float64(nums[pos])

		left := math.Floor(totalLeft / float64(pos+1))
		right := 0.0
		if pos < len(nums)-1 {
			right = math.Floor(totalRight / float64(len(nums)-pos-1))
		}

		averageDifference := math.Abs(left - right)

		if averageDifference < minAverageDifference {
			minAverageDifference = averageDifference
			minAverageDifferenceIndex = pos
		}
	}

	return minAverageDifferenceIndex
}
