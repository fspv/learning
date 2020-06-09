package main

import (
	"errors"
)

// TODO: add DP solution

func isSubsequence(s string, t string) bool {
	bisect := func(arr []int, val int) (int, error) {
		left, right := -1, len(arr)

		for middle := (left + right) / 2; left+1 < right; middle = (left + right) / 2 {
			if arr[middle] > val {
				right = middle
			} else {
				left = middle
			}
		}
		if right < len(arr) {
			return arr[right], nil
		}
		return -1, errors.New("")
	}

	charMap := map[rune][]int{}

	for pos, char := range t {
		if _, ok := charMap[char]; !ok {
			charMap[char] = []int{}
		}
		charMap[char] = append(charMap[char], pos)
	}

	prevPos := -1
	for _, char := range s {
		if nextPos, err := bisect(charMap[char], prevPos); err == nil {
			prevPos = nextPos
		} else {
			return false
		}
	}

	return true
}

func isSubsequenceGreedyTwoPointers(s string, t string) bool {
	if len(s) == 0 {
		return true
	}
	patternPtr := 0

	for strPtr := range t {
		if t[strPtr] == s[patternPtr] {
			patternPtr += 1
			if patternPtr == len(s) {
				return true
			}
		}
	}

	return false
}
