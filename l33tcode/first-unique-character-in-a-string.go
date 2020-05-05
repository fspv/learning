func firstUniqChar(s string) int {
	count := map[rune]int{}

	for _, char := range s {
		count[char] += 1
	}

	for pos, char := range s {
		if count[char] == 1 {
			return pos
		}
	}

	return -1
}
