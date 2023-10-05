package main

func majorityElement(nums []int) int {
	candidate, count := 0, 0

	for _, num := range nums {
		if count == 0 {
			candidate = num
			count += 1
		} else if num == candidate {
			count += 1
		} else {
			count -= 1
		}
	}

	return candidate
}
