package main

func numRabbits(answers []int) int {
    counts := map[int]int{}

	for _, answer := range answers {
		if _, ok := counts[answer+1]; !ok {
			counts[answer+1] = 0
		}
		counts[answer+1] += 1
	}

	result := 0

	for rabbits, count := range counts {
		tmp := count / rabbits
		if count % rabbits > 0 {
			tmp += 1
		}
		result += tmp * rabbits
	}

	return result
}
