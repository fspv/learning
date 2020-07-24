package main

func findDuplicate(nums []int) int {
	ptrSlow, ptrFast := nums[0], nums[nums[0]]

	for ptrSlow != ptrFast {
		ptrSlow = nums[ptrSlow]
		ptrFast = nums[ptrFast]
		ptrFast = nums[ptrFast]
	}

	ptrSlow = 0
	for ptrSlow != ptrFast {
		ptrSlow = nums[ptrSlow]
		ptrFast = nums[ptrFast]
	}

	return ptrSlow
}
