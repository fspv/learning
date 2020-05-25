package main

func findAnagrams(s string, p string) []int {
	counter := map[byte]int{}

	for pos := range p {
		counter[p[pos]]++
	}

	left, right := 0, 0

	result := []int{}

	for right < len(s) {
		count, right_count_ok := counter[s[right]]
		if right_count_ok && count > 0 {
			counter[s[right]]--
			right++
		} else {
			_, left_count_ok := counter[s[left]]
			if left_count_ok {
				counter[s[left]]++
			}
			left++
			if left > right {
				right = left
			}
		}
		if right-left == len(p) {
			result = append(result, left)
		}
	}

	return result
}
