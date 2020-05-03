package main

func canConstruct(ransomNote string, magazine string) bool {
	counter := map[rune]int{}

	for _, letter := range magazine {
		counter[letter] += 1
	}

	for _, letter := range ransomNote {
		if counter[letter] > 0 {
			counter[letter] -= 1
		} else {
			return false
		}
	}

	return true
}
