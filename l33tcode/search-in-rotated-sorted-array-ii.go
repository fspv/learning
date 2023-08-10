package main

func search2(nums []int, target int) bool {
	left, right := 0, len(nums)

	// Make sure nums[left] == nums[mid] == nums[right] is
	// impossible
	for left < right && nums[right-1] == nums[left] {
		right -= 1
	}

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

	return nums[(left+rotatedStart)%len(nums)] == target
}
