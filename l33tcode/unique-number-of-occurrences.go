package main

func uniqueOccurrences(arr []int) bool {
	occurences := map[int]int{}

	for _, num := range arr {
		if _, ok := occurences[num]; ok {
			occurences[num]++
		} else {
			occurences[num] = 1
		}
	}

	hashMap := map[int]bool{}

	for _, num := range occurences {
		if _, ok := hashMap[num]; ok {
			return false
		} else {
			hashMap[num] = true
		}
	}

	return true
}
