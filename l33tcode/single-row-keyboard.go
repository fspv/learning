package main

import "math"

func calculateTime(keyboard string, word string) int {
	cursor := 0

	keyToPos := map[rune]int{}

	for pos, char := range keyboard {
		keyToPos[char] = pos
	}

	distance := 0

	for _, char := range word {
		distance += int(math.Abs(float64(keyToPos[char]) - float64(cursor)))

		cursor = keyToPos[char]
	}

	return distance
}
