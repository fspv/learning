package main

func findAndReplacePattern(words []string, pattern string) []string {
	result := []string{}

	for _, word := range words {
		pat_to_word := map[byte]byte{}
		word_to_pat := map[byte]byte{}
		for pos, _ := range word {
			var ok bool
			_, ok = pat_to_word[pattern[pos]]
			if ok && word[pos] != pat_to_word[pattern[pos]] {
				break
			}

			_, ok = word_to_pat[word[pos]]
			if ok && pattern[pos] != word_to_pat[word[pos]] {
				break
			}

			pat_to_word[pattern[pos]] = word[pos]
			word_to_pat[word[pos]] = pattern[pos]

			if pos == len(word)-1 {
				result = append(result, word)
			}
		}
	}

	return result
}
