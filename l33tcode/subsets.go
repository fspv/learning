package main

func subsets(nums []int) [][]int {
	results := [][]int{}

	results = append(results, []int{})

	for _, num := range nums {
		for pos := range make([]bool, len(results)) {
			new_result := make([]int, len(results[pos]))
			copy(new_result, results[pos])
			new_result = append(new_result, num)
			results = append(results, new_result)
		}
	}

	return results
}
