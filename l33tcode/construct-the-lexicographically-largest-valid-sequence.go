package main

func constructDistancedSequenceDFS(pos int, n int, numMap map[int]int, seq []int) bool {
	if pos == len(seq) {
		for _, count := range numMap {
			if count > 0 {
				return false
			}
		}

		return true
	}

	if seq[pos] != 0 {
		return constructDistancedSequenceDFS(pos+1, n, numMap, seq)
	}

	for i := range make([]bool, n) {
		nextNum, count := n-i, numMap[n-i]
		if count == 0 {
			continue
		}

		distance := nextNum
		if nextNum == 1 {
			distance = 0
		}

		if pos+distance >= len(seq) || seq[pos+distance] != 0 {
			continue
		}

		numMap[nextNum] -= 1
		seq[pos], seq[pos+distance] = nextNum, nextNum

		if constructDistancedSequenceDFS(pos+1, n, numMap, seq) {
			return true
		}

		numMap[nextNum] += 1
		seq[pos], seq[pos+distance] = 0, 0

	}

	return false
}

func constructDistancedSequence(n int) []int {
	seq := make([]int, n*2-1)
	numMap := make(map[int]int, n)
	for i := range make([]bool, n) {
		numMap[i+1] = 1
	}

	constructDistancedSequenceDFS(0, n, numMap, seq)

	return seq
}
