func findDuplicates(nums []int) []int {
	result := []int{}
	for pos := range nums {
		num := nums[pos]
		if num < 0 {
			num *= -1
		}
		if nums[num-1] < 0 {
			result = append(result, num)
		}
		nums[num-1] *= -1
	}

	return result
}
