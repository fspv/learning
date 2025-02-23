package main

func findMaxConsecutiveOnes(nums []int) int {
	prevZeroOffset := 0
	maxCount, count := 0, 0

	for _, num := range nums {
		prevZeroOffset += 1

		if num == 1 {
			count += 1
		} else {
			count = prevZeroOffset
			prevZeroOffset = 0
		}

		if count > maxCount {
			maxCount = count
		}
	}

	return maxCount
}
