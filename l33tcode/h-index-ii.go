package main

func hIndex(citations []int) int {
	check := func(array []int, pos int) bool {
		// Checks if this position is to the left or to the right of h-index
		// false: left
		// true: right or here

		return array[pos] >= len(array)-pos
	}
	bisect := func(array []int) int {
		// find the leftmost position where number of citations greater or equal
		// then the number of elements to the right (including current)
		left, right := -1, len(array)
		middle := (left + right) / 2
		for ; middle != left && middle != right; middle = (left + right) / 2 {
			if check(array, middle) {
				right = middle
			} else {
				left = middle
			}
		}
		return right
	}

	return len(citations) - bisect(citations)
}
