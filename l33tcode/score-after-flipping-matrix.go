package main

func matrixScore(A [][]int) int {
	if len(A) == 0 {
		return 0
	}

	// Flip rows where first number is not 1
	for row := range A {
		flip := 1 - A[row][0]

		for col := range A[row] {
			A[row][col] = A[row][col] ^ flip
		}
	}

	// Flip columns where number of zeroes > number of ones
	for col := range A[0] {
		zeroes, ones := 0, 0
		for row := range A {
			if A[row][col] == 1 {
				ones += 1
			} else {
				zeroes += 1
			}
		}

		flip := 0
		if zeroes > ones {
			flip = 1
		}

		for row := range A {
			A[row][col] = A[row][col] ^ flip
		}
	}

	// Calculate the score
	score := 0
	for row := range A {
		number := 0
		for col := range A[row] {
			number += A[row][col]
			number <<= 1
		}
		score += number >> 1
	}

	return score
}
