package main

func groupThePeople(groupSizes []int) [][]int {
	groups := map[int][]int{}

	result := [][]int{}

	for pos, size := range groupSizes {
		_, ok := groups[size]
		if !ok {
			groups[size] = []int{}
		}
		groups[size] = append(groups[size], pos)
		if len(groups[size]) == size {
			result = append(result, groups[size])
			groups[size] = []int{}
		}
	}

	return result
}
