package main

func searchInsert(nums []int, target int) int {
	left, right := -1, len(nums)

	for middle := (left + right) / 2; left+1 < right; middle = (left + right) / 2 {
		if nums[middle] >= target {
			right = middle
		} else {
			left = middle
		}
	}

	return right
}
