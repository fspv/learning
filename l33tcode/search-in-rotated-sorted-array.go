package main

func search(nums []int, target int) int {
	left, right := 0, len(nums)

	for left < right {
		mid := left + (right-left)/2

		if nums[mid] >= nums[0] {
			left = mid + 1
		} else {
			right = mid
		}
	}

	rotatedStart := left % len(nums)

	left, right = 0, len(nums)-1

	for left < right {
		mid := left + (right-left)/2

		if nums[(mid+rotatedStart)%len(nums)] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	if pos := (left + rotatedStart) % len(nums); nums[pos] == target {
		return pos
	}

	return -1
}
