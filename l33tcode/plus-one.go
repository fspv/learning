package main

func plusOne(digits []int) []int {
	remain := 1
	revResult := []int{}

	for pos := range digits {
		revPos := len(digits) - pos - 1
		newNum := digits[revPos] + remain

		revResult = append(revResult, newNum%10)
		remain = newNum / 10
	}

	if remain == 1 {
		revResult = append(revResult, remain)
	}

	result := []int{}
	for pos := range revResult {
		revPos := len(revResult) - pos - 1
		result = append(result, revResult[revPos])
	}

	return result
}
