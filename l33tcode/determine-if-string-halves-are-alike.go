package main

func vowelsCount(arr string) int {
	vowels := map[rune]bool{
		'a': true, 'e': true, 'i': true, 'o': true, 'u': true, 'A': true, 'E': true, 'I': true, 'O': true, 'U': true,
	}

	result := 0

	for _, char := range arr {
		if _, ok := vowels[char]; ok {
			result += 1
		}
	}

	return result
}

func halvesAreAlike(s string) bool {
	countLeft := vowelsCount(s[:(len(s) / 2)])
	countRight := vowelsCount(s[(len(s) / 2):])

	return countLeft == countRight
}
