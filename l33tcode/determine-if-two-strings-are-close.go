package main

import "sort"

func closeStrings(word1 string, word2 string) bool {
	hashMap1 := map[rune]int{}
	hashMap2 := map[rune]int{}

	for _, char := range word1 {
		if _, ok := hashMap1[char]; !ok {
			hashMap1[char] = 0
		}

		hashMap1[char] += 1
	}

	for _, char := range word2 {
		if _, ok := hashMap1[char]; !ok {
			return false
		}

		if _, ok := hashMap2[char]; !ok {
			hashMap2[char] = 0
		}

		hashMap2[char] += 1
	}

	counts1 := []int{}
	counts2 := []int{}

	for char, count := range hashMap1 {
		if _, ok := hashMap2[char]; !ok {
			return false
		}

		counts1 = append(counts1, count)
	}

	for _, count := range hashMap2 {
		counts2 = append(counts2, count)
	}

	sort.Ints(counts1)
	sort.Ints(counts2)

	for pos, _ := range counts1 {
		if counts1[pos] != counts2[pos] {
			return false
		}
	}

	return true
}
