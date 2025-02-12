func maximumSum(nums []int) int {
	result := -1
	maxPrev := map[int]int{}

	for _, num := range nums {
		numCopy := num
		sumDigits := 0

		for numCopy > 0 {
			sumDigits = sumDigits + numCopy % 10
			numCopy = numCopy / 10
		}

		if prevNum, ok := maxPrev[sumDigits]; ok {
			if result < prevNum + num {
				result = prevNum + num
			}
			if prevNum < num {
				maxPrev[sumDigits] = num
			}
		} else {
			maxPrev[sumDigits] = num
		}
	}

	return result
}
